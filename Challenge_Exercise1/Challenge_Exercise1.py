# Project #1(A): An object inheriting from two different classes
class AnimalType:
    def eats(self):
        print("This animal likes to eat?")

class rabbits(AnimalType):
    def munch(self):
        print("carrots")

class birds(rabbits):
    def munch1(self):
        print("seeds")

class cats(AnimalType):
    def munch(self):
        print("fish")

RabbitObject = rabbits()
RabbitObject.eats()
RabbitObject.munch()

# here we have the Bird Object inheriting
# from two different classes
BirdObject = AnimalType()
BirdObject = birds()
BirdObject.eats()
BirdObject.munch1()

# add the 3rd animal
CatObject = cats()
CatObject.eats()
CatObject.munch()











