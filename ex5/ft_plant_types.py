



class Plant:

    name: str
    _height: float
    _age: int
    rate: float
    default_height: float = 0.1
    default_day: int = 0

    def __init__(self, name: str, _height: float, _age: int, rate: float = 0.8) -> None:
        self.name = name
        self.set_height(_height, 1)
        self.set_age(_age, 1)
        self.rate = rate
        print("Created: ", end = "")
        self.show()

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, _height: float, is_create: bool = 0) -> int:
        if(_height <= 0):
            print(f"{self.name}: Error, height can't be negative")
            if (is_create):
                print(f"Default height = {self.default_height}")
                self._height = self.default_height
                return -1
            print("Height update rejected")
            return -1 
        self._height = _height
        if (is_create == 0):
            print(f"Height updated: {round(self._height, 1)}cm")
        return 0

    def set_age(self, _age: int, is_create: bool = 0) -> int:
        if(_age <= 0):
            print(f"{self.name}: Error, age can't be negative")
            if (is_create):
                print(f"Default age = {self.default_day}")
                self._age = self.default_day
                return -1
            print("Age update rejected")
            return -1 
        self._age = _age
        if (is_create == 0):
            print(f"Age updated: {self._age} days")
        return 0

    def show(self) -> None:
        print(f"{self.name}: {round(self._height, 1)}cm, {self._age} days old ")

    def grow(self) -> None:
        self._height += self.rate

    def age(self) -> None:
        self._age += 1

    def simulate_week(self) -> None:
        start = self._height
        self.show()
        for i in range(1, 8):
            self.grow()
            self.age()
            print(f"\n=== Day {i} ===")
            self.show()
        print(f"\nGrowth this week: {round(self._height - start, 1)}cm")



class Flower(Plant):
    super.


def main() -> None:
    plant1 = Plant("Rose", 15, 10)
    print()
    plant1.set_height(25)
    plant1.set_age(30)
    print()
    plant1.set_height(-1)
    plant1.set_age(-1)
    print("\nCurrent state: ", end = "")
    plant1.show()

if __name__ == "__main__":
    print("\n=== Garden Plant Types ===\n")
    main()
    print("\n=== End of Program ===")

