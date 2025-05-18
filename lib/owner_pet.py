class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise TypeError("pet_type must be in PET_TYPES")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)


class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise TypeError("pet must be of Pet class")
        pet.owner = self

    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda x: x.name)



owner3 = Owner("kassim")
p7 = Pet("renny", "dog")
owner3.add_pet(p7)

sorted_owner = owner3.get_sorted_pets()
print(sorted_owner) 

# Pet instances (not yet assigned owners)
p1 = Pet("Rex", "dog")
p2 = Pet("Clark", "cat")
p3 = Pet("Becky", "rodent")
p4 = Pet("Kiwi", "bird")
p5 = Pet("Crocodile", "reptile")
p6 = Pet("Dorper", "exotic")
p7 = Pet("renny", "dog")
# Owner instances
owner1 = Owner("Titus")
owner2 = Owner("Alice")
owner3 = Owner("kassim")


# p1.owner = owner1
# p2.owner = owner1
# p3.owner = owner2


# print(owner1.pets())
# print(owner2.pets())

owner3.add_pet(p7)


# print(owner1.pets())
# print(owner3.pets())

# sorted pets by their names

sorted_owner = owner3.get_sorted_pets()
print(sorted_owner)
