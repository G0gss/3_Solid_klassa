class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_address(self):
        return self.address

class Student(Person):
    def __init__(self, name, age, address, school_name):
        super().__init__(name, age, address)
        self.school_name = school_name

    def get_school_name(self):
        return self.school_name

class Teacher(Person):
    def __init__(self, name, age, address, subject):
        super().__init__(name, age, address)
        self.subject = subject

    def get_subject(self):
        return self.subject