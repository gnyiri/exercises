class Animal:
    def __init__(self):
        self._position = 0

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        self._position = value

    def name(self) -> str:
        raise NotImplementedError

    def move(self):
        raise NotImplementedError


class Cat(Animal):
    def __init__(self):
        super().__init__()

    def name(self) -> str:
        return "Cat"

    def move(self):
        self._position = self._position + 1


class Dog(Animal):
    def __init__(self):
        super().__init__()

    def name(self) -> str:
        return "Dog"

    def move(self):
        self._position = self._position + 2


def move_animals(p_animals: list):
    for a in p_animals:
        old_position = a.position
        a.move()
        print("Move {} from {} to {}".format(a.name(), old_position, a.position))


if __name__ == '__main__':
    animals = [Dog(), Cat(), Dog(), Dog()]
    move_animals(animals)
