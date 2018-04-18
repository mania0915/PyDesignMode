#! /usr/bin/env python
# encoding=utf-8
class Burger():
    name=""
    price=0.0
    TYPE='BURGER'
    def getprice(self):
        return self.price
    def setPrice(self,price):
        self.price = price
    def getName(self):
        return self.Name


class cheeseBurger(Burger):
    def __init__(self):
        self.name='cheeseBurger'
        self.price=10.0

class spicyChickenBuiger(Burger):
    def __init__(self):
        self.name = 'spicyChicj=kenBurger'
        self.price = 12.0


class Snack():
    name=''
    price=''
    TYPE='SNACK'

    def getPrice(self):
        return self.name
    def setPrice(self,price):
        self.price = price
    def getName(self):
        return self.name

class Chips(Snack):
    def __init__(self,name,price):
        self.name='Chips'
        self.price = 1.0

class ChickenWings(Snack):
    def __init__(self):
        self.name = "chicken wings"
        self.price = 12.0


class FoodFactory():
    TYPE=""
    def creatFood(self,foodClass):
        print(self.TYPE , " factory produce a instance.")
        instance =  foodClass()
        return instance

class BurgerFactory(FoodFactory):
    def __init__(self):
        self.TYPE='BURGER'

class SnackFactory(FoodFactory):
    def __init__(self):
        self.TYPE="SNACK"
class SimpleFactory():
    @classmethod
    def createFood(cls,FoodClass):
        instance = FoodClass()
        return instance
if __name__ == '__main__':
    burgeFactory = BurgerFactory()
    snackFactory = SnackFactory()
    cheese_burger = burgeFactory.creatFood(cheeseBurger)
    chickenWings = snackFactory.creatFood(ChickenWings)
    print(cheese_burger.name,cheese_burger.price)
    print(chickenWings.name,chickenWings.price)



    pass