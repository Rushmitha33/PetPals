from entity.pet import Pet

class Cat(Pet):
    def __init__(self, name: str, age: int, breed: str, cat_color: str):
        super().__init__(name, age, breed)
        self.cat_color = cat_color

    def __str__(self):
        return super().__str__() + f", Cat Color: {self.cat_color}"
