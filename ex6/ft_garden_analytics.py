
class Plant:
    name: str
    _height: float
    _age: int
    default_height: float = 0.1
    default_day: int = 0
    stats: "Stats"

    class Stats:
        _grow_count: int = 0
        _age_count: int = 0
        _show_count: int = 0

        def __init__(self) -> None:
            pass

        def increase_grow(self) -> None:
            self._grow_count += 1

        def increase_age(self) -> None:
            self._age_count += 1

        def increase_show(self) -> None:
            self._show_count += 1

        def display(self) -> None:
            print("Stats: ", end="")
            print(f"{self._grow_count} grow, ", end="")
            print(f"{self._age_count} age, ", end="")
            print(f"{self._show_count} show")

    @staticmethod
    def is_older_than_year(age: int) -> bool:
        is_older = age > 365
        print(f"Is {age} days more than a year? -> {is_older}")
        return is_older

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0, 0)

    def __init__(self, name: str, _height: float, _age: int) -> None:
        self.name = name
        self.set_height(_height, True)
        self.set_age(_age, True)
        self.stats = self.Stats()

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, _height: float, is_create: bool = False) -> int:
        if (_height <= 0):
            print(f"{self.name}: Error, height can't be negative")
            if (is_create):
                print(f"Default height = {self.default_height}")
                self._height = self.default_height
                return -1
            print("Height update rejected")
            return -1
        self._height = _height
        if (not is_create):
            print(f"Height updated: {round(self._height, 1)}cm")
        return 0

    def set_age(self, _age: int, is_create: bool = False) -> int:
        if (_age <= 0):
            print(f"{self.name}: Error, age can't be negative")
            if (is_create):
                print(f"Default age = {self.default_day}")
                self._age = self.default_day
                return -1
            print("Age update rejected")
            return -1
        self._age = _age
        if (not is_create):
            print(f"Age updated: {self._age} days")
        return 0

    def show(self) -> None:
        self.stats.increase_show()
        print(f"{self.name}: {round(self._height, 1)}cm, {self._age} days old")

    def grow(self, rate: float = 0.8) -> None:
        self.stats.increase_grow()
        self._height += rate

    def age(self, day: int = 1) -> None:
        self.stats.increase_age()
        self._age += day

    def simulate_week(self, rate: float = 0.8) -> None:
        start = self._height
        self.show()
        for i in range(1, 8):
            self.grow(rate)
            self.age()
            print(f"\n=== Day {i} ===")
            self.show()
        print(f"\nGrowth this week: {round(self._height - start, 1)}cm")


class Flower(Plant):
    color: str
    is_bloomed: bool = False

    def __init__(self, name: str, _h: float, _a: int, color: str) -> None:
        super().__init__(name, _h, _a)
        self.color = color

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if (self.is_bloomed):
            print(" Rose is blooming beautifully!")
        else:
            print(" Rose has not bloomed yet")

    def bloom(self) -> None:
        self.is_bloomed = True


class Seed(Flower):
    seed: int = 0

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self.seed}")

    def bloom(self) -> None:
        super().bloom()
        self.seed = 42


class Tree(Plant):
    is_shade: bool = False
    t_diameter: float
    stats: "Stats"

    class Stats(Plant.Stats):
        _shade_count: int = 0

        def increase_shade(self) -> None:
            self._shade_count += 1

        def display(self) -> None:
            super().display()
            print(f"{self._shade_count} shade")

    def __init__(self, name: str, _h: float, _a: int, t_d: float) -> None:
        super().__init__(name, _h, _a)
        self.t_diameter = t_d
        self.stats = self.Stats()

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {round(self.t_diameter, 1)}")

    def produce_shade(self) -> None:
        self.is_shade = True
        self.stats.increase_shade()
        print(" Tree Oak now produces a shade of ", end="")
        print(f"{round(self._height, 1)}.0cm long and ", end="")
        print(f"{round(self.t_diameter, 1)}cm wide.")


class Vegetable(Plant):
    season: str
    value: int = 0

    def __init__(self, name: str, _h: float, _a: int, season: str) -> None:
        super().__init__(name, _h, _a)
        self.season = season

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self.season}")
        print(f" Nutritional value: {self.value}")

    def grow(self, rate: float = 0.8) -> None:
        super().grow(rate)
        self.value += 1


def main() -> None:

    print("=== Check year-old")
    Flower.is_older_than_year(30)
    Flower.is_older_than_year(400)

    print("\n=== Flower")
    rose = Flower("Rose", 15, 10, "Red")
    rose.show()
    print("[statistics for Rose]")
    rose.stats.display()
    print("[asking the rose to grow and bloom]")
    rose.grow(8)
    rose.bloom()
    rose.show()
    rose.stats.display()

    print("\n=== Tree")
    oak = Tree("Oak", 200, 365, 5)
    oak.show()
    oak.stats.display()
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    oak.stats.display()

    print("\n=== Seed")
    sun = Seed("Sunflower", 80, 45, "yellow")
    sun.show()
    print("[make sunflower grow, age and bloom]")
    sun.age(20)
    sun.grow(30)
    sun.bloom()
    sun.show()
    print("[statistics for Sunflower]")
    sun.stats.display()

    print("\n=== Anonymous")
    anonymous = Plant.create_anonymous()
    anonymous.show()
    anonymous.stats.display()


if __name__ == "__main__":
    print("\n=== Garden statistics ===\n")
    main()
    print("\n=== End of Program ===")
