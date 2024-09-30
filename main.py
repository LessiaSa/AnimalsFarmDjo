class Animals():
    def __init__(self, name, weight,voice,food):
        self.name = name
        self.weight = weight
        self.voice = voice
        self.food = food
        Animals.total_weight = 0
        Animals.heaviest_animal = None

    def voice(self, says):
        self.voice()

    def product(self):
        pass


class MilkGivers(Animals):
    def milking(self):
        print(f'получаем молоко от {self.name}')
    def product(self):
        self.milking()

class Haircuts(Animals):
    def wool(self):
        print(f'получаем шерсть от {self.name}')
    def product(self):
        self.wool()

class LayingEggs(Animals):
   def eggs(self):
       print(f'собираем яйца у {self.name}')
   def product(self):
       self.eggs()

class Geese(LayingEggs):
   def __init__(self,name,weight):
       super().__init__(name, weight, "Га-га-га","трава")

class Cows(MilkGivers):
    def __init__(self, name, weight):
        super().__init__(name, weight, "Мууу", "сено")

class  Sheep(Haircuts):
    def __init__(self, name, weight):
        super().__init__(name, weight, "Беее", "трава")

class Chicken(LayingEggs):
    def __init__(self, name, weight):
        super().__init__(name, weight, "Ко-ко-ко", "зерно")

class Goats(MilkGivers):
    def __init__(self, name, weight):
        super().__init__(name, weight, "Меее", "сено")

class Ducks(LayingEggs):
    def __init__(self, name, weight):
        super().__init__(name, weight, "Кря-кря-кря", "трава, зерно, рыбка")



goose1 = Geese("Серый", 5)
goose2 = Geese("Белый", 4)
cow = Cows("Манька", 795)
sheep1 = Sheep("Барашек", 35)
sheep2 = Sheep("Кудрявый", 31)
chicken1 = Chicken("Ко-ко", 2)
chicken2 = Chicken("кукареку", 3)
goat1 = Goats("Рога", 29)
goat2 = Goats("Копыта", 33)
duck = Ducks("Кряква", 3)

animals = [goose1, goose2, cow, sheep1, sheep2, chicken1, chicken2, goat1, goat2, duck]

for animal in animals:
    print(animal.name, animal.weight, animal.voice,animal.food, animal.product())

for animal in animals:
    Animals.total_weight = Animals.total_weight + animal.weight
print('\nОбщий вес всех животных: {} '.format(Animals.total_weight))

for animal in animals:
    if Animals.heaviest_animal is None:
        Animals.heaviest_animal = animal
    elif animal.weight > Animals.heaviest_animal.weight:
        Animals.heaviest_animal = animal
print(f'Самое тяжёлое животное: {Animals.heaviest_animal.name}, весит: {Animals.heaviest_animal.weight} кг')
