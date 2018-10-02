# ---------------------------------------------
#  ALL THE CODE BELLOW USES PYTHON 2 SYNTAX
# ---------------------------------------------

# CREATING A CLASS WITH A CONTRUCTOR (__init__):
class Person(object):
    __name = ''
    __lastName = ''
    
    def __init__(self, name, lastName):
        self.__name = name
        self.__lastName = lastName
    
    def info(self):
        return "Person's name: {}\nPerson's last name: {}".format(self.__name, self.__lastName)

p1 = Person('Gustavo', 'Pires')

print(p1.info())

# CREATING ANOTHER CLASS THAT INHERITS THE ABOVE CLASS:
class Customer(Person):
    __balance = 0
    
    def __init__(self, name, lastName, balance):
        # USING METHODS FROM THE INHERITED CLASS:
        super(Customer, self).__init__(name, lastName)
        self.__balance = balance
    
    def getCustomer(self):
        # RETURNING 
        return "\n{}\nCurrent balance: {}".format(Person.info(self), self.__balance)

p2 = Customer('Theo', 'Pires', 120)

print(p2.getCustomer())