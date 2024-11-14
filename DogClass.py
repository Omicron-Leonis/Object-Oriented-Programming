# create class
class Dog:

    #class attribute
    species = "domestic animal"
    #instance attribute
    def __init__(self, name,species):
        self.name = name
        self.species = species
#instantiate the Dog class
Bunty = Dog("Bunty", "German Shepherd")
Leo = Dog("Leo", "Poodle")

# access the class attributes
print("Bunty is a {}".format(Bunty.species))
print("Leo is also a {}".format(Leo.species))

#access the instance attributes
print("{} is a {}".format(Bunty.name, Bunty.species))
print("{} is a {} ".format(Leo.name, Leo.species)) 