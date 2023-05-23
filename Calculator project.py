# HW3
# REMINDER: The work in this assignment must be your own original work and must be completed alone.

from cmath import e
from xml.etree.ElementTree import tostring

class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return "Node({})".format(self.value) 

    __repr__ = __str__
                          

#=============================================== Part I ==============================================

class Stack:
    '''
        >>> x=Stack()
        >>> x.pop()
        >>> x.push(2)
        >>> x.push(4)
        >>> x.push(6)
        >>> x
        Top:Node(6)
        Stack:
        6
        4
        2
        >>> x.pop()
        6
        >>> x
        Top:Node(4)
        Stack:
        4
        2
        >>> len(x)
        2
        >>> x.peek()
        4
    '''
     
    def __init__(self):
        self.top = None
 

    def __str__(self):
        temp=self.top
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out='\n'.join(out)
        return ('Top:{}\nStack:\n{}'.format(self.top,out))

    __repr__=__str__


    def isEmpty(self):
        # YOUR CODE STARTS HERE
        return self.top == None 
    #goes through and counts the stack
    def __len__(self): 
        # YOUR CODE STARTS HERE
        count = 0 
        current = self.top 
        while current: 
            count += 1
            current = current.next 
        return count
            



    def push(self,value):
        # YOUR CODE STARTS HERE
        temp = Node(value)
        if self.isEmpty():
             self.top = temp 
        else: 
            temp.next = self.top
            self.top = temp
    #finds the top value, saves it as a variable, returns that and points the top to what was before
    def pop(self):
        # YOUR CODE STARTS HERE
        if self.isEmpty():
            return None 
        else: 
            rval = self.top.value 
            self.top = self.top.next 
            return rval 
            

    def peek(self):
        # YOUR CODE STARTS HERE
        if self.isEmpty():
            return None 
        else: 
            tval = self.top.value 
            return tval 


#=============================================== Part II ==============================================

class Calculator:
    def __init__(self):
        self.__expr = None


    @property
    def getExpr(self):
        return self.__expr

    def setExpr(self, new_expr):
        if isinstance(new_expr, str):
            self.__expr=new_expr
        else:
            print('setExpr error: Invalid expression')
            return None
    #if it returns error when trying to check if the string is a float, we know its not a number
    def _isNumber(self, txt):
        '''
            >>> x=Calculator()
            >>> x._isNumber(' 2.560 ')
            True
            >>> x._isNumber('7 56')
            False
            >>> x._isNumber('2.56p')
            False
        '''
        # YOUR CODE STARTS HERE
        try:
            float(txt)
            return True 
        except: 
            return False


    #helper method that converts the string expression into a list seperated by operators and operands
    def exptolst(self, txt):
        operators = ['+', '*', '/', '^', '(', ')']
        numbers = ['0','1','2','3','4','5','6','7','8','9','.']
        explst1 = ['']
        #goes through each character and if its an operator (not negative because it can be start of a number) and adds to list
        for char in txt: 
            if char in operators:
                explst1 += [char, '']
        #if -, then adds to list by itself
            elif char == '-': 
                explst1 += [char]
            elif char in numbers:
                explst1[-1] += char
        #takes care of empty spaces 
        explst2 = []
        for i in explst1: 
            if i.strip():
                explst2.append(i)
        


        return explst2

    
    #checks of the expression is valid by looking at if there are consecutive numbers or operators, or if the number of parenthesis was balanced or not
    def isvalid(self,lst):
        operatorsnp = ['+', '*', '/', '^']
        prev = None
        curr = None
        bal = 0
        #prev and curr are used to check the value at the current moment and the value be

        for i in range(len(lst)):
            #list of operators no parenthesis
            
            if i > 1:
                prev = lst[i-1]
            curr = lst[i]
            if curr == '(':
                bal +=1 
            if curr == ')':
                bal -= 1 
            #checks if there is an uneven amount of parenthesis 
            if bal <0: 
                return False
            #rest checks for special cases
            if len(curr) >1 and not self._isNumber(curr):
                return False
            #consecutive operators not allwoed
            if prev in operatorsnp and curr in operatorsnp: 
                return False 
            #consecutive numbers not allowed
            if self._isNumber(prev) and self._isNumber(curr): 
                return False
            #operator and closing parenthesis not allowed
            if prev in operatorsnp and curr == ')':
                return False 
            #number right before opening parenthesis not allowed
            if self._isNumber(prev) and curr == '(':
                return False 
            # )( is invalid, cannot multiply that way 
            if prev == ')' and curr == '(':
                return False 
        #if last element is operator 
        if lst[-1] in '+-*/^':
            return False
        
        #checks for balance mentioned earlier
        if bal == 0: 
            return True 
        else: 
            return False 
        
#failed to figure out how to do this for expressons with multiple/overlapping parenthesis like 
    def _getPostfix(self, txt):
        '''
        Required: _getPostfix must create and use a Stack for expression processing
            >>> x=Calculator()
            >>> x._getPostfix('     2 ^       4')
            '2.0 4.0 ^'
            >>> x._getPostfix('          2 ')
            '2.0'
            >>> x._getPostfix('2.1        * 5        + 3       ^ 2 +         1 +             4.45')
            '2.1 5.0 * 3.0 2.0 ^ + 1.0 + 4.45 +'
            >>> x._getPostfix('2*5.34+3^2+1+4')
            '2.0 5.34 * 3.0 2.0 ^ + 1.0 + 4.0 +'
            >>> x._getPostfix('2.1 * 5 + 3 ^ 2 + 1 + 4')
            '2.1 5.0 * 3.0 2.0 ^ + 1.0 + 4.0 +'
            >>> x._getPostfix('( .5 )')
            '0.5'
            >>> x._getPostfix ('( ( 2 ) )')
            '2.0'
            >>> x._getPostfix ('2 * (           ( 5 +-3 ) ^ 2 + (1 + 4 ))')
            '2.0 5.0 -3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x._getPostfix ('(2 * ( ( 5 + 3) ^ 2 + (1 + 4 )))')
            '2.0 5.0 3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x._getPostfix ('((2 *((5 + 3  ) ^ 2 + (1 +4 ))    ))')
            '2.0 5.0 3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x._getPostfix('2* (       -5 + 3 ) ^2+ ( 1 +4 )')
            '2.0 -5.0 3.0 + 2.0 ^ * 1.0 4.0 + +'

        # In invalid expressions, you might print an error message, adjust doctest accordingly
        # If you are veryfing the expression in calculate before passing to postfix, this cases are not necessary

            >>> x._getPostfix('2 * 5 + 3 ^ + -2 + 1 + 4')
            >>> x._getPostfix('     2 * 5 + 3  ^ * 2 + 1 + 4')
            >>> x._getPostfix('2    5')
            >>> x._getPostfix('25 +')
            >>> x._getPostfix(' 2 * ( 5      + 3 ) ^ 2 + ( 1 +4 ')
            >>> x._getPostfix(' 2 * ( 5 + 3 ) ^  2 + ) 1 + 4 (')
            >>> x._getPostfix('2 *      5% + 3       ^ + -2 +1 +4')
        '''

        # YOUR CODE STARTS HERE
        postfixStack = Stack()  # method must use postfixStack to compute the postfix expression
        post = []
        #made the priority of operands into easily accesable dictonary and parenthesis have lowest precidence 
        precedence = {'+':1, '-': 1, '*': 2, '/': 2, '^': 3, '(': 0}
        operatorsnp = ['+', '*', '/', '^'] #does not have - as it can be start of a number
        #this is the converted expression list
        self.setExpr(txt)
        expressionlist = self.exptolst(txt)

        if expressionlist == 'invalid':
            return None

        balance = 0

        #checks if expression is valid 
        if self.isvalid(expressionlist) == False: 
            return None 

        #if its a number, gets added to the postfix list normally
        for i in expressionlist:
            if self._isNumber(i): 
                num = str(float(i))
                post.append(num)
        #if its an open parenthesis, I put into stack and it makes it so we have a signal for where the parenthesis started, treating this like its own expression
            elif i == '(': 
                balance +=1 

                postfixStack.push(i)
        #when I find the ending parenthesis, I put the contents back out into postfix notation until i find the original parenthesis 
            elif i == ')':
                #checks if stack is empty to avoid looping forever  
                while not postfixStack.isEmpty() and postfixStack.peek() != '(':
                    ret = postfixStack.pop()
                    post.append(ret)
                postfixStack.pop()
        #if stack is empty, push into stack, otherwise pop two elenents out calculate for it as covered by last lecture video 
            elif i in operatorsnp and postfixStack.isEmpty(): 
                postfixStack.push(i)
            elif i in operatorsnp: 
        #nop is the new and prevop is the previous item from the stack which 
                nop = precedence[i]
                prevop = precedence[postfixStack.peek()]
                while prevop >= nop and postfixStack.isEmpty() == False: 
                    prevop = precedence[postfixStack.peek()]
                    ret = postfixStack.pop()
                    post.append(ret)
                postfixStack.push(i)
        #finish up by emptying stack into postfix list 
        if postfixStack.isEmpty() == False: 
            while postfixStack.isEmpty() == False: 
                ret = postfixStack.pop()
                post.append(ret)
        finalpost = ' '.join(post)
        #getting rid of the open parenthesis from postfix notation 
        return finalpost.replace('( ', '')

    
            
    @property
    def calculate(self):
        '''
            calculate must call _getPostfix
            calculate must create and use a Stack to compute the final result as shown in the video lecture
            
            >>> x=Calculator()
            >>> x.setExpr('4        + 3 -       2')
            >>> x.calculate
            5.0
            >>> x.setExpr('-2 +          3.5')
            >>> x.calculate
            1.5
            >>> x.setExpr('      4 +           3.65  - 2        / 2')
            >>> x.calculate
            6.65
            >>> x.setExpr('23 / 12 - 223 + 5.25      * 4 * 3423')
            >>> x.calculate
            71661.91666666667
            >>> x.setExpr('2-3*4')
            >>> x.calculate
            -10.0
            >>> x.setExpr('7^2^3')
            >>> x.calculate
            5764801.0
            >>> x.setExpr(' 3 * ((( 10 - 2*3 )) )')
            >>> x.calculate
            12.0
            >>> x.setExpr('      8 / 4 * (3 - 2.45 * ( 4   - 2 ^ 3 )       ) + 3')
            >>> x.calculate
            28.6
            >>> x.setExpr('2 * ( 4 +        2 * (         5 - 3 ^ 2 ) + 1 ) + 4')
            >>> x.calculate
            -2.0
            >>> x.setExpr(' 2.5 +         3 * (2 + ( 3.0) * ( 5^2-2 * 3 ^ ( 2 )         ) * ( 4 ) ) * ( 2 / 8 + 2 * ( 3 - 1 /3 ) ) - 2 / 3^ 2')
            >>> x.calculate
            1442.7777777777778
            

            # In invalid expressions, you might print an error message, but code must return None, adjust doctest accordingly
            >>> x.setExpr(" 4 ++ 3+ 2") 
            >>> x.calculate
            >>> x.setExpr("4  3 +2")
            >>> x.calculate
            >>> x.setExpr('( 2 ) * 10 - 3 *( 2 - 3 * 2 ) )')
            >>> x.calculate
            >>> x.setExpr('( 2 ) * 10 - 3 * / ( 2 - 3 * 2 )')
            >>> x.calculate
            >>> x.setExpr(' ) 2 ( *10 - 3 * ( 2 - 3 * 2 ) ')
            >>> x.calculate
            >>> x.setExpr('(    3.5 ) ( 15 )') 
            >>> x.calculate
            >>> x.setExpr('3 ( 5) - 15 + 85 ( 12)') 
            >>> x.calculate
            >>> x.setExpr("( -2/6) + ( 5 ( ( 9.4 )))") 
            >>> x.calculate
        '''

        if not isinstance(self.__expr,str) or len(self.__expr)<=0:
            print("Argument error in calculate")
            return None
        #not entirely sure why there are still so many failures, i'm sure my logid is right 
        
        calcStack = Stack()   # method must use calcStack to compute the  expression

        # YOUR CODE STARTS HERE
        postfix = self._getPostfix(self.getExpr)
        #postfix can return None so I exit out if there is an error 
        if postfix == None: 
            return None 
        tocalc = postfix.split()
        #now that we have the expression in postfix, we just perform the respective operations from the stack 
        for char in tocalc: 
            if self._isNumber(char): 
                calcStack.push(char)
            else: 
        #Important to convert to float and know that second actually comes before the first because of last in first out
                second = float(calcStack.pop())
                first = float(calcStack.pop())
                
                if char == '^': 
                    calcStack.push(first ** second)
                elif char == '*': 
                    calcStack.push(first * second)
                elif char == '/': 
                    calcStack.push(first / second)
                elif char == '+': 
                    calcStack.push(first + second)
                elif char == '-': 
                    calcStack.push(first - second)

        result = calcStack.pop()
        
        return result

        

#=============================================== Part III ==============================================

class AdvancedCalculator:
    '''
        >>> C = AdvancedCalculator()
        >>> C.states == {}
        True
        >>> C.setExpression('a = 5;b = 7 + a;a = 7;c = a + b;c = a * 0;return c')
        >>> C.calculateExpressions() == {'a = 5': {'a': 5.0}, 'b = 7 + a': {'a': 5.0, 'b': 12.0}, 'a = 7': {'a': 7.0, 'b': 12.0}, 'c = a + b': {'a': 7.0, 'b': 12.0, 'c': 19.0}, 'c = a * 0': {'a': 7.0, 'b': 12.0, 'c': 0.0}, '_return_': 0.0}
        True
        >>> C.states == {'a': 7.0, 'b': 12.0, 'c': 0.0}
        True
        >>> C.setExpression('x1 = 5;x2 = 7 * ( x1 - 1 );x1 = x2 - x1;return x2 + x1 ^ 3')
        >>> C.states == {}
        True
        >>> C.calculateExpressions() == {'x1 = 5': {'x1': 5.0}, 'x2 = 7 * ( x1 - 1 )': {'x1': 5.0, 'x2': 28.0}, 'x1 = x2 - x1': {'x1': 23.0, 'x2': 28.0}, '_return_': 12195.0}
        True
        >>> print(C.calculateExpressions())
        {'x1 = 5': {'x1': 5.0}, 'x2 = 7 * ( x1 - 1 )': {'x1': 5.0, 'x2': 28.0}, 'x1 = x2 - x1': {'x1': 23.0, 'x2': 28.0}, '_return_': 12195.0}
        >>> C.states == {'x1': 23.0, 'x2': 28.0}
        True
        >>> C.setExpression('x1 = 5 * 5 + 97;x2 = 7 * ( x1 / 2 );x1 = x2 * 7 / x1;return x1 * ( x2 - 5 )')
        >>> C.calculateExpressions() == {'x1 = 5 * 5 + 97': {'x1': 122.0}, 'x2 = 7 * ( x1 / 2 )': {'x1': 122.0, 'x2': 427.0}, 'x1 = x2 * 7 / x1': {'x1': 24.5, 'x2': 427.0}, '_return_': 10339.0}
        True
        >>> C.states == {'x1': 24.5, 'x2': 427.0}
        True
        >>> C.setExpression('A = 1;B = A + 9;C = A + B;A = 20;D = A + B + C;return D - A')
        >>> C.calculateExpressions() == {'A = 1': {'A': 1.0}, 'B = A + 9': {'A': 1.0, 'B': 10.0}, 'C = A + B': {'A': 1.0, 'B': 10.0, 'C': 11.0}, 'A = 20': {'A': 20.0, 'B': 10.0, 'C': 11.0}, 'D = A + B + C': {'A': 20.0, 'B': 10.0, 'C': 11.0, 'D': 41.0}, '_return_': 21.0}
        True
        >>> C.states == {'A': 20.0, 'B': 10.0, 'C': 11.0, 'D': 41.0}
        True
        >>> C.setExpression('A = 1;B = A + 9;2C = A + B;A = 20;D = A + B + C;return D + A')
        >>> C.calculateExpressions() is None
        True
        >>> C.states == {}
        True
    '''
    def __init__(self):
        self.expressions = ''
        self.states = {}

    def setExpression(self, expression):
        self.expressions = expression
        self.states = {}

    def _isVariable(self, word):
        '''
            >>> C = AdvancedCalculator()
            >>> C._isVariable('volume')
            True
            >>> C._isVariable('4volume')
            False
            >>> C._isVariable('volume2')
            True
            >>> C._isVariable('vol%2')
            False
        '''
        # YOUR CODE STARTS HERE

        #checks first if the input is in a string format
        if isinstance(word, str):
        #then if the first letter is actually a letter        
            if word[:1].isalpha(): 
        #then if the rest if alphanumeric
                if word.isalnum():
                    return True 
                else: 
                    return False
            else: 
                return False
        else: 
            return False
       

    def _replaceVariables(self, expr):
        '''
            >>> C = AdvancedCalculator()
            >>> C.states = {'x1': 23.0, 'x2': 28.0}
            >>> C._replaceVariables('1')
            '1'
            >>> C._replaceVariables('105 + x')
            >>> C._replaceVariables('7 * ( x1 - 1 )')
            '7 * ( 23.0 - 1 )'
            >>> C._replaceVariables('x2 - x1')
            '28.0 - 23.0'
        '''
        # YOUR CODE STARTS HERE
        newexp = expr.split(' ')
        #checks if the element if a variable, then checks if it is a valid variable, and if it is then replaces the element with the value
        for i in range(len(newexp)): 
            if self._isVariable(newexp[i]):
                if newexp[i] in self.states.keys(): 
                    newexp[i] = str(self.states[newexp[i]])
                else: 
                    return None 
        #joining the list back into a string 
        newexplst = ' '.join(newexp)
        return newexplst

    def calculateExpressions(self):
        self.states = {} 
        calcObj = Calculator()     # method must use calcObj to compute each expression
        # YOUR CODE STARTS HERE
        newdict = {}
        eqlst = self.expressions.split(';')
        for item in (eqlst):
            #this if statement only fires when I have reached the end of the expression, as it always has 'r' as the first character
            if item[0] == 'r': 
                #splits the last item so that its a blank element and the other one is the variable
                finalp = item[7:]
                #setting the expression and getting it ready to evaluate
                replaced = (self._replaceVariables(finalp))
                if replaced == None: 
                    self.state = {}
                    return None
                calcObj.setExpr(replaced)
                final = calcObj.calculate
                #hardcoding the final portion because I'm not sure how else to, and the output matches up
                newdict['_return_'] = float(final)
            else: 
                #variable, value is what varval stands for. 
                varval = item.split(' = ')
                ##setting the key/value or variable/value pair here and then replacing variables and getting it ready to calculate so that it can be one solid value
                newval = self._replaceVariables(varval[1])
                if newval == None: 
                    self.state.clear()
                    return None
                calcObj.setExpr(newval)
                calcexp = calcObj.calculate
                #setting calculated value equal to the variable in self.states
                
                self.states[varval[0]] = float(calcexp)
                #putting that as its own item in the new dictonary, which will be my final output and then coppying again and repeating the process 
                newdict[item] = self.states.copy()


            
        return newdict



                

                
            



_test_calc = Calculator.calculate
#_test_postfix = Calculator._getPostfix()


if __name__=='__main__':
    import doctest
    doctest.testmod()
    #doctest.run_docstring_examples(Calculator.calculate, globals(), name='HW3',verbose=True)