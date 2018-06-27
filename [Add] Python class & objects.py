
# coding: utf-8

# https://www.youtube.com/watch?v=ZDa-Z5JzLYM&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc

# # class and instances

# - Don't forget to add 'self' when creating methods
# - Don't forget to add parenthesis when calling methods
# 

# In[1]:


class Employee:
    
# initialize class attributes
    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.email = fname + '_' + lname + '@andrew.cmu.edu'
        
# create class method        
# self is instance argument
    def get_name(self):
        print('{} {}'.format(self.fname, self.lname))
        


# In[2]:


# create instance
emp_1 = Employee('Ling','Hong',3000)

# print out attributes
print(emp_1.pay)
print(emp_1.email)

# call class method
emp_1.get_name()

# pass the instance argument to the class method
# it's equal to emp_1.get_name()
Employee.get_name(emp_1)


# # class var and instance var

# - class variables are shared by all instances
# 
# - when creating methods that involve class variables, we can choose to access the class variable through
#  (1) class
#  so that the method cannot be overridden by instances
#  (2) instance
#  so that the method cannot be overridden by instances
# 
# - we can check class variables and instance variables by printing out __dict__
# 
# - we can change the value of class variable for only one instance by accessing it through the instance (e.g. emp_1.var=3). Then the variable will become an instance variable

# In[3]:


class Employee_1:
# class variables
    raise_per = 1.04
    num_employees = 0
    
# initialize class attributes
    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.email = fname + '_' + lname + '@andrew.cmu.edu'
        
        # use Employee_1 so that it can't be overridden by instances
        Employee_1.num_employees += 1
        
# create class method        
# self is instance argument
    def get_name(self):
        print('{} {}'.format(self.fname, self.lname))

# when acessing the class variable, we need to access it through class or instance
    def raise_pay(self):
        # use self.raise_per so that it can be overridden by instance
        self.pay = int(self.pay * self.raise_per)
       


# In[4]:


emp_2 = Employee_1('Lynne','Pastor', 5000)
print(emp_2.pay)
emp_2.raise_pay()
print(emp_2.pay)

# access class variable through class
print(Employee_1.raise_per)
# access class variable through instance
print(emp_2.raise_per)


# In[5]:


# check instance variables
print(emp_2.__dict__)
print('\n')

# check class variables (and class methods)
print(Employee_1.__dict__)


# In[6]:


# change class attributes through class
Employee_1.raise_per = 1.05
print(Employee_1.raise_per)
print(emp_2.raise_per)

# change class attributes through one instance
emp_2.raise_per = 1.06
print(Employee_1.raise_per)
print(emp_2.raise_per)

# create an attribute called 'raise_per' for that instance
print(emp_2.__dict__)


# # Regular methods, Static methods, Class methods

# - regular method automatically takes instance (self) as the first arguement
# - class method automatically takes class (cls) as the first arguement
# - static method don't pass anything automatically
# 
# - to turn regular method into class method, add class method decorator @classmethod
# - even when using static method, you need to access it through the class
# 

# In[7]:


class Employee_2:
    raise_per = 1.04    
    num_employees = 0
    
    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.email = fname.lower() + '_' + lname.lower() + '@andrew.cmu.edu'
        Employee_2.num_employees += 1
    
    def get_name(self):
        return '{} {}'.format(self.fname, self.lname)
    
    def raise_pay(self):
        self.pay = int(self.pay * self.raise_per)
    
    @classmethod
    def set_raise_per(cls, amount):
        cls.raise_per = amount
    
    @classmethod
    # allow people to use a string to create instances
    def from_string(cls, emp_string):
        fname, lname, pay = emp_string.split('-')
        return cls(fname, lname, pay)
        
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True   


# In[8]:


Employee_2.set_raise_per(1.07)
print(Employee_2.raise_per)


# In[9]:


# accept a string to create instances
emp_string = 'Emily-Simmons-6700'
emp_3 = Employee_2.from_string(emp_string)
print(emp_3.email)


# In[10]:


import datetime
my_date = datetime.date(2018,7,1)

# don't forget to add class before the static method
print(Employee_2.is_workday(my_date))


# # Inheritance and subclass

# - don't forget to inherit the method when initializing -- super().__init__
# - use print(help(Class)) to get more info
# - use isinstance() and issubclass() to check the relationship
# 

# In[11]:


class Developer(Employee_2):
    raise_per = 1.1
    
    # add new attributes -- programming language
    def __init__(self, fname, lname, pay, prog_lang):
        
        # inheritance
        super().__init__(fname, lname, pay)
        
        self.prog_lang = prog_lang


# In[12]:


dev_1 = Developer('Ted','Tso',9000,'Python')

print(dev_1.pay)
dev_1.raise_pay()
print(dev_1.pay)

print(Developer.raise_per)

print(dev_1.prog_lang)


# In[13]:


# use help to check more details
print(help(Developer))


# In[14]:


class Manager(Employee_2):
    def __init__(self, fname, lname, pay, employees=None):
        super().__init__(fname, lname, pay)
        
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    
    def add_employees(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_employees(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    
    def print_emps(self):
        for emp in self.employees:
            emp.get_name()      


# In[15]:


mgr_1 = Manager('Sue','Smith',100000,[emp_2,dev_1])
print(mgr_1.email)
print('\n')

mgr_1.print_emps()
print('\n')

mgr_1.add_employees(emp_1)
mgr_1.print_emps()


# In[16]:


# check is an instance or not
print(isinstance(mgr_1, Manager))
print(isinstance(mgr_1, Employee_2))
print(isinstance(mgr_1, Developer))

# check is a subclass or not
print(issubclass(Manager, Employee_2))
print(issubclass(Manager, Developer))


# # Special and magic methods

# - the system will call str() first. If the method does not exist, it will then call repr()

# In[17]:


class Employee_2:
    raise_per = 1.04    
    num_employees = 0
    
    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.email = fname.lower() + '_' + lname.lower() + '@andrew.cmu.edu'
        Employee_2.num_employees += 1
    
    def get_name(self):
        return '{} {}'.format(self.fname, self.lname)
    
    def raise_pay(self):
        self.pay = int(self.pay * self.raise_per)
    
    @classmethod
    def set_raise_per(cls, amount):
        cls.raise_per = amount
    
    @classmethod
    # allow people to use a string to create instances
    def from_string(cls, emp_string):
        fname, lname, pay = emp_string.split('-')
        return cls(fname, lname, pay)
        
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True   
    
    def __repr__(self):
        return 'Employee_2({},{},{})'.format(self.fname, self.lname, self.pay)
    
    def __str__(self):
        return '{} - {}'.format(self.get_name(), self.email)
    
    def __add__(self, other):
        return self.pay + other.pay
    
    def __len__(self):
        return len(self.get_name())


# In[28]:


emp_4 = Employee_2('Jenny','Lutz',6000)
emp_5 = Employee_2('Jennie','Lutz',6001)
print(emp_4)
print(repr(emp_4))
print(str(emp_4))
print(len(emp_4))
print(emp_4+emp_5)
print(len(emp_4))


# In[19]:


# other arithmetic special methods
print(1+2)
print('1'+'2')
print(int.__add__(1,2))
print(str.__add__('1','2'))

# using len() method on objects
print(len('test'))
print('test'.__len__())


# # Property decorator

# property decorator allows us to access a method like an attribute

# In[20]:


# the email is not updated automatically 
class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        self.email = fname.lower() + '_' + lname.lower() + '@andrew.cmu.edu'
    
    def fullname(self):
        return '{} {}'.format(self.fname, self.lname)


# In[21]:


emp_test = Employee('Johnn', 'Smith')
print(emp_test.fullname())
print(emp_test.email)

emp_test.fname = 'John'
print(emp_test.fullname())
print(emp_test.email)


# In[22]:


# one solution to let the email is  updated automatically 
# change email from an attribute to a method
#  but people who are using this class need to change their codes -- use email() instead of email
class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    
    def email(self):
        return '{}_{}@andrew.cmu.edu'.format(self.fname,self.lname)
    
    def fullname(self):
        return '{} {}'.format(self.fname, self.lname)


# In[23]:


emp_test = Employee('Johnn', 'Smith')
print(emp_test.fullname())
print(emp_test.email())

emp_test.fname = 'John'
print(emp_test.fullname())
print(emp_test.email())


# In[24]:


# another solution to let the email is  updated automatically 
# use property decorator so that we can access methods like attirbutes
# use setter we can not only access methods like attributes, but also modify them like attributes
# use deleter we can delete attributes through the method

class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        
    @property
    def email(self):
        return '{}_{}@andrew.cmu.edu'.format(self.fname,self.lname)
    
    @property
    def fullname(self):
        return '{} {}'.format(self.fname, self.lname)
    @fullname.setter
    def fullname(self,name):
        fname, lname = name.split(' ')
        self.fname = fname
        self.lname = lname
    @fullname.deleter
    def fullname(self):
        print('Delete!')
        self.fname = None
        self.lname = None


# In[25]:


emp_test = Employee('Johnn', 'Smith')
print(emp_test.fullname)
print(emp_test.email)

emp_test.fname = 'John'
print(emp_test.fullname)
print(emp_test.email)

emp_test.fullname = 'Jim Smith'
print(emp_test.fname)

del emp_test.fullname
print(emp_test.fname)


# # Generator

# - Sometimes the list is so large that merely creating it would consume all of the system's memory. 
# - To work around this, one may want to be able to call get_primes with a start value and get all the primes larger than start
# - generator can simply return the next value instead of all the values at once. It wouldn't need to create a list at all. No list, no memory issues. 
# - If the body of a def contains yield, the function automatically becomes a generator function (even if it also contains a return statement).
# - To be considered an iterator, generators must define a few methods, one of which is __next__(). 
# - To get the next value from a generator, we use the same built-in function as for iterators: next().
# -  You can "send" values to a generator using the generator's send method.

# In[53]:


# an ordinary iterable
# a list that stores prime numbers
import math
def get_prime(num_list):
    prime_list = [i for i in num_list if is_prime()]
    return prime_list

def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(number) + 1), 2):
            if number % current == 0: 
                return False
        return True
    return False


# In[54]:


# a simple generator 
def simple_generator():
    yield 1
    yield 2
    yield 3

# one way to use it : print out
for value in simple_generator():
    print(value)

# another way to use it : next()
num_gen = simple_generator()
next(num_gen)
next(num_gen)


# In[60]:


# generator version
# num is the start number
# use while True so that it won't hit the end of iteration if the first number is not a prime number
def prime_gen(num):
    while True:
        if is_prime(num):
            yield num
        num = num + 1

prime_gen_test = prime_gen(10)
print(next(prime_gen_test))
print(next(prime_gen_test))
print(next(prime_gen_test))
print(next(prime_gen_test))
print(next(prime_gen_test))


# In[88]:


# to set an upper limit
# if there is no upper limit, the loop will run forever to infinite when you are iterating over the prime_gen_test
def prime_gen(num,upper=100):
    while num<=upper:
        if is_prime(num):
            yield num
        num = num + 1

prime_gen_test = prime_gen(10,100)

for value in prime_gen_test:
    print(value)
    
# after we have exhausted all the numbers in the iterable, the 'StopIteration' will be raised
next(prime_gen_test)


# In[89]:


# if we want to restart, we can create a new generator
prime_gen_test2 = prime_gen(10,100)
next(prime_gen_test2)


# In[90]:


# we'll find the smallest prime number greater than successive powers of a number 
# for 10, we want the smallest prime greater than 10, then 100, then 1000, etc.

def successive_prime(base, power_limit):
    prime_list = []
    for power in range(1,power_limit+1):
        start = base**power
        prime_generator = prime_gen(start,100)
        prime_list.append(next(prime_generator))
    return prime_list


# In[91]:


successive_prime(2,5)


# # why send() is not working??

# In[92]:


#  You can "send" values to a generator using the generator's send method
# iteration is a list of power
'''
When you're using send to "start" a generator (that is, execute the code from the first line of the generator 
function up to the first yield statement) you must send None.
'''

def successive_prime(iterations, base):
    prime_generator = prime_gen(base)
    prime_generator.send(None)
    for power in iterations:
        print(prime_generator.send(base**power))


# In[93]:


successive_prime([1,2,3,4,5], 2)


# In[103]:


def odd_gen(num):
    while True:
        if num%2!=0:
            yield num
        num = num + 1


# In[104]:


def continuous_odd(base, power_list):
    odd_generator = odd_gen(base)
    odd_generator.send(None)
    result_list = []
    for power in power_list:
        result_list.append(odd_generator.send(base**power))
    return result_list
        


# In[105]:


a = continuous_odd(10,[1,2,3,4,5])
a


# In[ ]:


a = continuous_odd(10,[1,2,3,4,5])
a

