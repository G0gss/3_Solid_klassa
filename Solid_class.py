class Person: 
    def __init__(self, name, age, address): # __init__ принимает аргументы name, age, address
        self.name = name                    # три метода: get_name, get_age, get_address. Они возвращают соответствующие атрибуты объекта.
        self.age = age
        self.address = address

    def get_name(self): # Создаются 3 метода представленных ниже, они возращают соответствующие атрибуты объекта.
        return self.name

    def get_age(self):
        return self.age

    def get_address(self):
        return self.address

class Student(Person):
    def __init__(self, name, age, address, school_name): # __init__` принимает четыре аргумента: name, age, address, school_name
        super().__init__(name, age, address) # вызываетcя метод __init__ класса Person c помощью функции super, передавая аргументы name, age, address
        self.school_name = school_name # создаётся новый аргумент school_name.

    def get_school_name(self): # Создаётся метод который возращает атрибут school_name
        return self.school_name

class Teacher(Person): 
    def __init__(self, name, age, address, subject): # __init__` принимает четыре аргумента: name, age, address, subject
        super().__init__(name, age, address) # Вызвали метод __init__ и с помощью функции super пережади аргументы name, age, address
        self.subject = subject # создаётся новый аргумент subject.

    def get_subject(self): # Создаётся метод который возращает атрибут subject
        return self.subject
