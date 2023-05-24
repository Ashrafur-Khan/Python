
import random



class Course:
    '''
        >>> c1 = Course('CMPSC132', 'Programming in Python II', 3)
        >>> c2 = Course('CMPSC360', 'Discrete Mathematics', 3)
        >>> c1 == c2
        False
        >>> c3 = Course('CMPSC132', 'Programming in Python II', 3)
        >>> c1 == c3
        True
        >>> c1
        CMPSC132(3): Programming in Python II
        >>> c2
        CMPSC360(3): Discrete Mathematics
        >>> c3
        CMPSC132(3): Programming in Python II
        >>> c1 == None
        False
        >>> print(c1)
        CMPSC132(3): Programming in Python II
    '''
    def __init__(self, cid, cname, credits):
        # YOUR CODE STARTS HERE
        self.cid = cid
        self.cname = cname
        self.credits = credits


    def __str__(self):
        # YOUR CODE STARTS HERE
        return f'{self.cid}({self.credits}): {self.cname}'

    __repr__ = __str__

    def __eq__(self, other):
        # YOUR CODE STARTS HERE
        if hasattr(other,'cid'): 
            if self.cid == other.cid: 
                return True 
            else: 
                return False
        else: 
            return False 



class Catalog:
    ''' 
        >>> C = Catalog()
        >>> C.courseOfferings
        {}
        >>> C._loadCatalog("cmpsc_catalog_small.csv")
        >>> C.courseOfferings
        {'CMPSC 132': CMPSC 132(3): Programming and Computation II, 'MATH 230': MATH 230(4): Calculus and Vector Analysis, 'PHYS 213': PHYS 213(2): General Physics, 'CMPEN 270': CMPEN 270(4): Digital Design, 'CMPSC 311': CMPSC 311(3): Introduction to Systems Programming, 'CMPSC 360': CMPSC 360(3): Discrete Mathematics for Computer Science}
        >>> C.removeCourse('CMPSC 360')
        'Course removed successfully'
        >>> C.courseOfferings
        {'CMPSC 132': CMPSC 132(3): Programming and Computation II, 'MATH 230': MATH 230(4): Calculus and Vector Analysis, 'PHYS 213': PHYS 213(2): General Physics, 'CMPEN 270': CMPEN 270(4): Digital Design, 'CMPSC 311': CMPSC 311(3): Introduction to Systems Programming}
        >>> isinstance(C.courseOfferings['CMPSC 132'], Course)
        True
    '''

    def __init__(self):
        # YOUR CODE STARTS HERE
        self.courseOfferings={}

    def addCourse(self, cid, cname, credits):
        # YOUR CODE STARTS HERE
        if cid in self.courseOfferings:
            return 'Course already added'
        else: 
            self.courseOfferings[cid] =  Course(cid,cname,credits)
            return 'Course added successfully'

    def removeCourse(self, cid):
        # YOUR CODE STARTS HERE
        if cid in self.courseOfferings:
            self.courseOfferings.pop(cid)
            return 'Course removed successfully'
        else: 
            return 'Course not found'

    def _loadCatalog(self, file):
        with open(file, "r") as f:
            course_info = f.read()

        new=course_info.split('\n') #first putting everything into one big string
        for i in new: 
            nl=i.split(',') #seperating each into a list so that I can then call for specific elements and put into Course
            self.courseOfferings[nl[0]] = Course(nl[0],nl[1],int(nl[2])) #Course gives me the format I want and its not a string





class Semester:
    '''
        >>> cmpsc131 = Course('CMPSC 131', 'Programming in Python I', 3)
        >>> cmpsc132 = Course('CMPSC 132', 'Programming in Python II', 3)
        >>> math230 = Course("MATH 230", 'Calculus', 4)
        >>> phys213 = Course("PHYS 213", 'General Physics', 2)
        >>> econ102 = Course("ECON 102", 'Intro to Economics', 3)
        >>> phil119 = Course("PHIL 119", 'Ethical Leadership', 3)
        >>> spr22 = Semester()
        >>> spr22
        No courses
        >>> spr22.addCourse(cmpsc132)
        >>> isinstance(spr22.courses['CMPSC 132'], Course)
        True
        >>> spr22.addCourse(math230)
        >>> spr22
        CMPSC 132; MATH 230
        >>> spr22.isFullTime
        False
        >>> spr22.totalCredits
        7
        >>> spr22.addCourse(phys213)
        >>> spr22.addCourse(econ102)
        >>> spr22.addCourse(econ102)
        'Course already added'
        >>> spr22.addCourse(phil119)
        >>> spr22.isFullTime
        True
        >>> spr22.dropCourse(phil119)
        >>> spr22.addCourse(Course("JAPNS 001", 'Japanese I', 4))
        >>> spr22.totalCredits
        16
        >>> spr22.dropCourse(cmpsc131)
        'No such course'
        >>> spr22.courses
        {'CMPSC 132': CMPSC 132(3): Programming in Python II, 'MATH 230': MATH 230(4): Calculus, 'PHYS 213': PHYS 213(2): General Physics, 'ECON 102': ECON 102(3): Intro to Economics, 'JAPNS 001': JAPNS 001(4): Japanese I}
    '''


    def __init__(self):
        # --- YOUR CODE STARTS HERE
        self.courses = {}


    def __str__(self):
        nl=[]
        if len(self.courses.keys()) == 0: 
            return 'No courses'
        for course in self.courses: 
            nl+=[self.courses[course].cid] #first I put all elements/info from the desired course in a list,
        full = "; ".join(nl) #then I just join them and make it into a string to return 
        return full

    __repr__ = __str__

    def addCourse(self, course):
        # YOUR CODE STARTS HERE
        if course.cid in self.courses:
            return 'Course already added'
        else: 
            self.courses[course.cid] = Course(course.cid, course.cname, course.credits) #similar to catalog
            

    def dropCourse(self, course):
        # YOUR CODE STARTS HERE
        if course.cid in self.courses: 
            del self.courses[course.cid] #this completly deletes the key and its values from the dict
        else: 
            return 'No such course'


    @property
    def totalCredits(self):
        # YOUR CODE STARTS HERE
        credits=0
        for course in self.courses: 
            cinstance = self.courses[course] 
            credits += cinstance.credits #pulls the credits from the desired courses 
        return credits 

    @property
    def isFullTime(self):
        # YOUR CODE STARTS HERE
        credits=0
        for course in self.courses: 
            credits += (self.courses[course]).credits
        if credits < 12:
            return False
        else: 
            return True 

    
class Loan:
    '''
        >>> import random
        >>> random.seed(2)  # Setting seed to a fixed value, so you can predict what numbers the random module will generate
        >>> first_loan = Loan(4000)
        >>> first_loan
        Balance: $4000
        >>> first_loan.loan_id
        17412
        >>> second_loan = Loan(6000)
        >>> second_loan.amount
        6000
        >>> second_loan.loan_id
        22004
        >>> third_loan = Loan(1000)
        >>> third_loan.loan_id
        21124
    '''
    

    def __init__(self, amount):
        # YOUR CODE STARTS HERE
        self.amount = amount
        self.loan_id = self.__getloanID

    def __str__(self):
        # YOUR CODE STARTS HERE
        return f'Balance: ${self.amount}'

    __repr__ = __str__


    @property
    def __getloanID(self):
        # YOUR CODE STARTS HERE
        loan_id = random.randint(10000,90000)
        return loan_id

class Person:
    '''
        >>> p1 = Person('Jason Lee', '204-99-2890')
        >>> p2 = Person('Karen Lee', '247-01-2670')
        >>> p1
        Person(Jason Lee, ***-**-2890)
        >>> p2
        Person(Karen Lee, ***-**-2670)
        >>> p3 = Person('Karen Smith', '247-01-2670')
        >>> p3
        Person(Karen Smith, ***-**-2670)
        >>> p2 == p3
        True
        >>> p1 == p2
        False
    '''

    def __init__(self, name, ssn):
        # YOUR CODE STARTS HERE
        self.name = name
        self.ssn = ssn

    def __str__(self):
        # YOUR CODE STARTS HERE
        last4=self.get_ssn()[-4:] #last 4 digits of ssn from splicing the whole thing
        return f'Person({self.name}, ***-**-{last4})'

    __repr__ = __str__

    def get_ssn(self):
        # YOUR CODE STARTS HERE
        return self.ssn

    def __eq__(self, other):
        # YOUR CODE STARTS HERE
        if self.get_ssn() == other.get_ssn(): #gets and compares ssn of both
            return True 
        else: 
            return False

class Staff(Person):
    '''
        >>> C = Catalog()
        >>> C._loadCatalog("cmpsc_catalog_small.csv")
        >>> s1 = Staff('Jane Doe', '214-49-2890')
        >>> s1.getSupervisor
        >>> s2 = Staff('John Doe', '614-49-6590', s1)
        >>> s2.getSupervisor
        Staff(Jane Doe, 905jd2890)
        >>> s1 == s2
        False
        >>> s2.id
        '905jd6590'
        >>> p = Person('Jason Smith', '221-11-2629')
        >>> st1 = s1.createStudent(p)
        >>> isinstance(st1, Student)
        True
        >>> s2.applyHold(st1)
        'Completed!'
        >>> st1.registerSemester()
        'Unsuccessful operation'
        >>> s2.removeHold(st1)
        'Completed!'
        >>> st1.registerSemester()
        >>> st1.enrollCourse('CMPSC 132', C)
        'Course added successfully'
        >>> st1.semesters
        {1: CMPSC 132}
        >>> s1.applyHold(st1)
        'Completed!'
        >>> st1.enrollCourse('CMPSC 360', C)
        'Unsuccessful operation'
        >>> st1.semesters
        {1: CMPSC 132}
    '''
    def __init__(self, name, ssn, supervisor=None):
        # YOUR CODE STARTS HERE
        self.name = name
        self.ssn = ssn
        self.supervisor = supervisor

    def __str__(self):
        # YOUR CODE STARTS HERE
        return f'Staff({self.name}, {self.id})'

    __repr__ = __str__


    @property
    def id(self):
        # YOUR CODE STARTS HERE
        nam=self.name.split()
        return f'905{(nam[0][0]).lower()}{(nam[1][0]).lower()}{self.get_ssn()[-4:]}'

    @property   
    def getSupervisor(self):
        # YOUR CODE STARTS HERE
        return self.supervisor

    def setSupervisor(self, new_supervisor):
        # YOUR CODE STARTS HERE
        if isinstance(new_supervisor, Staff): 
            self.supervisor = new_supervisor
            return 'Completed!'
        else: 
            return None


    def applyHold(self, student):
        # YOUR CODE STARTS HERE
        if isinstance(student, Student):
            student.hold = True
            return 'Completed!'
        else: 
            return None 


    def removeHold(self, student):
        # YOUR CODE STARTS HERE
        if isinstance(student, Student):
            student.hold = False
            return 'Completed!'
            
        else: 
            return None

    def unenrollStudent(self, student):
        # YOUR CODE STARTS HERE
        if isinstance(student, Student):
            student.active = False
        else: 
            return None

    def createStudent(self, person):
        # YOUR CODE STARTS HERE
        return Student(person.name, person.ssn, 'Freshman') 
         





class Student(Person):
    '''
        >>> C = Catalog()
        >>> C._loadCatalog("cmpsc_catalog_small.csv")
        >>> s1 = Student('Jason Lee', '204-99-2890', 'Freshman')
        >>> s1
        Student(Jason Lee, jl2890, Freshman)
        >>> s2 = Student('Karen Lee', '247-01-2670', 'Freshman')
        >>> s2
        Student(Karen Lee, kl2670, Freshman)
        >>> s1 == s2
        False
        >>> s1.id
        'jl2890'
        >>> s2.id
        'kl2670'
        >>> s1.registerSemester()
        >>> s1.enrollCourse('CMPSC 132', C)
        'Course added successfully'
        >>> s1.semesters
        {1: CMPSC 132}
        >>> s1.enrollCourse('CMPSC 360', C)
        'Course added successfully'
        >>> s1.enrollCourse('CMPSC 465', C)
        'Course not found'
        >>> s1.semesters
        {1: CMPSC 132; CMPSC 360}
        >>> s2.semesters
        {}
        >>> s1.enrollCourse('CMPSC 132', C)
        'Course already enrolled'
        >>> s1.dropCourse('CMPSC 360')
        'Course dropped successfully'
        >>> s1.dropCourse('CMPSC 360')
        'Course not found'
        >>> s1.semesters
        {1: CMPSC 132}
        >>> s1.registerSemester()
        >>> s1.semesters
        {1: CMPSC 132, 2: No courses}
        >>> s1.enrollCourse('CMPSC 360', C)
        'Course added successfully'
        >>> s1.semesters
        {1: CMPSC 132, 2: CMPSC 360}
        >>> s1.registerSemester()
        >>> s1.semesters
        {1: CMPSC 132, 2: CMPSC 360, 3: No courses}
        >>> s1
        Student(Jason Lee, jl2890, Sophomore)
        >>> s1.classCode
        'Sophomore'
    '''

    def __init__(self, name, ssn, year):
        random.seed(1)
        # YOUR CODE STARTS HERE
        self.name = name
        self.ssn = ssn 
        self.classCode = year 
        self.semesters = {}
        self.hold = False 
        self.active = True 
        self.account = self.__createStudentAccount()




    def __str__(self):
        # YOUR CODE STARTS HERE
        return f'Student({self.name}, {self.id}, {self.classCode})'

    __repr__ = __str__

    def __createStudentAccount(self):
        # YOUR CODE STARTS HERE
        if self.active == True: 
            return StudentAccount(self)
        else: 
            return None


    @property
    def id(self):
        # YOUR CODE STARTS HERE
        nam=self.name.split()
        return f'{(nam[0][0]).lower()}{(nam[1][0]).lower()}{self.get_ssn()[-4:]}'

    def registerSemester(self):
        # YOUR CODE STARTS HERE         
        
        lenkey=len(self.semesters)        #Assigns the grade here 
        if lenkey >= 6:
            self.classCode = 'Senior'
        elif  lenkey == 4 or lenkey == 5: 
            self.classCode = 'Junior'
        elif lenkey == 3 or lenkey == 4: 
            self.classCode = 'Sophomore'
        else: 
            self.classCode = 'Freshman'

        if self.active == True and  self.hold == False:
            if   len(self.semesters) == 0: 
                self.semesters[1]=Semester()
            else: 
                maxk = max(self.semesters.keys())+1 #Using formula from hw pdf
                self.semesters[maxk] = Semester()

                lenkey=len(self.semesters)
                
                if lenkey >= 6:                #Updates grade based on if they got another semester
                    self.classCode = 'Senior'
                elif  lenkey == 4 or lenkey == 5: 
                    self.classCode = 'Junior'
                elif lenkey == 3 or lenkey == 4: 
                    self.classCode = 'Sophomore'
                else: 
                    self.classCode = 'Freshman'
        else: 
            
            return 'Unsuccessful operation'

            


    def enrollCourse(self, cid, catalog):
        # YOUR CODE STARTS HERE
        maxk = max(self.semesters.keys()) 
        if cid in self.semesters[maxk].courses: #if its already in the semester
            return 'Course already enrolled'
        if self.active == True and self.hold == False: 
            for id in catalog.courseOfferings: 
                if id == cid: #goes through the entire catalog to see if the course is even there with if statement
                    self.semesters[maxk].courses[cid] = catalog.courseOfferings[id] 
                    self.account.chargeAccount(StudentAccount.CREDIT_PRICE*self.semesters[maxk].courses[cid].credits)
                    #first into the semester, then its courses, then its specific course to drop, then finds its credits
                    return 'Course added successfully'
            else: 
                return 'Course not found'
        else: 
            return 'Unsuccessful operation'

    def dropCourse(self, cid):
        # YOUR CODE STARTS HERE
        maxk = max(self.semesters.keys())
        
        if self.active == True and self.hold == False:
            
            if cid in self.semesters[maxk].courses: #similar to enroll
                self.account.makePayment((StudentAccount.CREDIT_PRICE*self.semesters[maxk].courses[cid].credits)*.5)
                #same as enroll
                del self.semesters[maxk].courses[cid] #was not sure if pop works here so I deleted to be safe
                return 'Course dropped successfully'
            else: 
                return 'Course not found'
        else: 
            return 'Unsuccessful operation'

    def getLoan(self, amount):
        # YOUR CODE STARTS HERE
        maxk = max(self.semesters.keys())
        if self.active == False: 
            return 'Unsuccessful operation'
        elif self.semesters[maxk].totalCredits < 12: #totalCredits lets me know if full time or not
            return 'Not full-time'
        else: 
            l=Loan(amount) 
            self.account.makePayment(l.amount)
            self.account.loans[l.loan_id] = l


class StudentAccount:
    '''
        >>> C = Catalog()
        >>> C._loadCatalog("cmpsc_catalog_small.csv")
        >>> s1 = Student('Jason Lee', '204-99-2890', 'Freshman')
        >>> s1.registerSemester()
        >>> s1.enrollCourse('CMPSC 132', C)
        'Course added successfully'
        >>> s1.account.balance
        3000
        >>> s1.enrollCourse('CMPSC 360', C)
        'Course added successfully'
        >>> s1.account.balance
        6000
        >>> s1.enrollCourse('MATH 230', C)
        'Course added successfully'
        >>> s1.enrollCourse('PHYS 213', C)
        'Course added successfully'
        >>> print(s1.account)
        Name: Jason Lee
        ID: jl2890
        Balance: $12000
        >>> s1.account.chargeAccount(100)
        12100
        >>> s1.account.balance
        12100
        >>> s1.account.makePayment(200)
        11900
        >>> s1.getLoan(4000)
        >>> s1.account.balance
        7900
        >>> s1.getLoan(8000)
        >>> s1.account.balance
        -100
        >>> s1.enrollCourse('CMPEN 270', C)
        'Course added successfully'
        >>> s1.account.balance
        3900
        >>> s1.dropCourse('CMPEN 270')
        'Course dropped successfully'
        >>> s1.account.balance
        1900.0
        >>> s1.account.loans
        {27611: Balance: $4000, 84606: Balance: $8000}
        >>> StudentAccount.CREDIT_PRICE = 1500
        >>> s2 = Student('Thomas Wang', '123-45-6789', 'Freshman')
        >>> s2.registerSemester()
        >>> s2.enrollCourse('CMPSC 132', C)
        'Course added successfully'
        >>> s2.account.balance
        4500
        >>> s1.enrollCourse('CMPEN 270', C)
        'Course added successfully'
        >>> s1.account.balance
        7900.0
    '''
    CREDIT_PRICE = 1000

    def __init__(self, student):
        # YOUR CODE STARTS HERE
        self.student = student
        self.balance = 0 
        self.loans = {}


    def __str__(self):
        # YOUR CODE STARTS HERE
        return f'Name: {self.student.name}\nID: {self.student.id}\nBalance: ${self.balance}'

    __repr__ = __str__


    def makePayment(self, amount):
        # YOUR CODE STARTS HERE
        self.balance -= amount
        return self.balance
            

    def chargeAccount(self, amount):
        # YOUR CODE STARTS HERE
        self.balance += amount 
        return self.balance




if __name__=='__main__':
    import doctest
    doctest.testmod(verbose=True)  # OR
    doctest.run_docstring_examples(StudentAccount, globals(), name='HW2',verbose=True) # replace Course for the class name you want to tes
