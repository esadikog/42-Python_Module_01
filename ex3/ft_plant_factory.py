
class Plant:

    name: str
    height: float
    agee: int
    rate: float

    def __init__(self, name: str, height: float, agee: int, rate: float = 0.8) -> None:
        self.name = name
        self.height = float(height)
        self.agee = agee
        self.rate = rate
        print("Created: ", end = "")
        self.show()

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}cm, {self.agee} days old ")

    def grow(self) -> None:
        self.height += self.rate

    def age(self) -> None:
        self.agee += 1

    def simulate_week(self) -> None:
        start = self.height
        self.show()
        for i in range(1, 8):
            self.grow()
            self.age()
            print(f"\n=== Day {i} ===")
            self.show()
        print(f"\nGrowth this week: {round(self.height - start, 1)}cm")



def main() -> None:
    plant1 = Plant("Rose", 25.0, 30)
    plant2 = Plant("Oak", 200.0, 365)
    plant3 = Plant("Cactus", 5.0, 90)
    plant4 = Plant("Sunflower", 80.0, 45)
    plant5 = Plant("Fern", 15, 120)

if __name__ == "__main__":
    print("\n=== Plant Factory Output ===\n")
    main()
    print("\n=== End of Program ===")