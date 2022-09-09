class Person():
    def __init__(self, name, age):
        self.age = age
        self.name = name

    def say_hello(self):
        print(f'Hello {self.name}, you are {self.age} years old')


if __name__ == '__main__':
    person = Person('Ricardo', 43)

    print(person.say_hello())
