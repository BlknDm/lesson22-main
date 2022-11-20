# Измените класс Person так, чтобы его методы 
# оперировали внутренним состоянием, 
# а не использовали цепочку вызовов объектов

class Person:
    def __init__(self, population, num_room):
        self.population = population
        self.num_room = num_room

    def get_room(self):
        return self.num_room

    def get_population(self):
        return self.population


John = Person(100500, 3)
Mary = Person(100501, 5)
print(John.get_room())
print(John.get_population())