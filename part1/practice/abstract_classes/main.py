# Создайте абстрактный класс автомобиля Transport c абстрактными методами
# - start_engine
# - stop_engine
# - move
# - stop

from abc import ABC, abstractmethod


class Transport(ABC):

    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def stop(self):
        pass
# Унаследуйте от него три класса Boat, Car, Electroscooter
# для каждого из требуемых методов через print укажите какое-либо действие.
# К примеру start_engine -> print('Двигатель катера запущен')

class Boat(Transport):
    def start_engine(self):
        print('Катер загудел, забурлила вода')

    def stop_engine(self):
        print('Двигатели катера чихнули, булькнула вода')

    def move(self):
        print('Нос катера приподнялся, катер двинулся вперед, разрезая водную гладь, создавая волны')

    def stop(self):
        print('Катер остановился')


class Car(Transport):
    def start_engine(self):
        print('Мощно заурчала V-образная восьмерка')

    def stop_engine(self):
        print('Двигатель заглушен')

    def move(self):
        print('Автомобиль с пробуксовкой помчался к месту назначения')

    def stop(self):
        print('Автомобиль припаркован')


class Electroscooter(Transport):
    def start_engine(self):
        print('Мигнул светодиодом')

    def stop_engine(self):
        print('Мигнул светодиодом дважды')

    def move(self):
        print('Прохожие в ужасе разбегаются от очередного камикадзе')

    def stop(self):
        print('Торможение об стену прошло успешно')


class Person:
    def use_transport(self, transport: Transport):
        transport.start_engine()
        transport.move()
        transport.stop()
        transport.stop_engine()


if __name__ == '__main__':
    boat = Boat()
    car = Car()
    kamikadze = Electroscooter()

    person = Person()
    person.use_transport(boat)
    print('=' * 10)
    person.use_transport(car)
    print('=' * 10)
    person.use_transport(kamikadze)
