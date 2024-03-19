class Owner:
    def __init__(self, name):
        self.name = name
        self.pets_list = []

    def pets(self):
        return self.pets_list

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Pet type is invalid!")
        pet.set_owner(self)
        self.pets_list.append(pet)

    def get_sorted_pets(self):
        sorted_pets = sorted(self.pets_list, key=lambda x: x.name)
        return sorted_pets


class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in self.PET_TYPES:
            raise Exception("Pet type is invalid!")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        if owner:
            owner.add_pet(self)
        self.all.append(self)

    def set_owner(self, owner):
        if not isinstance(owner, Owner):
            raise Exception("Invalid owner type!")
        self.owner = owner
