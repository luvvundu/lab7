class IncorrectTriangleSides(Exception):
    pass

class Triangle:
    def __init__(self, side1, side2, side3):
        if side1 <= 0 or side2 <= 0 or side3 <= 0:
            raise IncorrectTriangleSides("Стороны должны быть положительными")
        if side1 + side2 <= side3 or side1 + side3 <= side2 or side2 + side3 <= side1:
            raise IncorrectTriangleSides("Ссума двух сторон не может быть меньше 3 стороны")

        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def triangle_type(self):
        if self.side1 == self.side2 == self.side3:
            return "equilateral"
        elif self.side1 == self.side2 or self.side1 == self.side3 or self.side2 == self.side3:
            return "isosceles"
        else:
            return "nonequilateral"

    def perimeter(self):
        return self.side1 + self.side2 + self.side3


try:
    triangle = Triangle(3, 4, 5)
    print("Triangle Type:", triangle.triangle_type())
    print("Perimeter:", triangle.perimeter())
except IncorrectTriangleSides as e:
    print("Error:", e)