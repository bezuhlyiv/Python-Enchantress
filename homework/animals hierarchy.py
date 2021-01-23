class Animal:
    def __init__(self, live):
        self.live = live

    def run(self):
        pass


class Dog(Animal):
    def bark(self):
        pass


class Cat(Animal):
    def meow(self):
        pass


class PersianCat(Cat):
    def sleep(self):
        pass


class WildCat(Cat):
    def survive(self):
        pass


class CatDog(Dog, Cat):
    def sleep(self):
        pass
