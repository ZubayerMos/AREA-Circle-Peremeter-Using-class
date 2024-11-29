class Area ():
    def __init__(self,pie,r):
        self.pie = pie
        self.r = r

class Circle(Area):
    def __init__(self, pie, r):
        super().__init__(pie, r)
pie_2 = 3.1416
r1 = int(input("Enter a number : "))
circle = Circle(pie_2,r1)
circle_2 = pie_2*r1*r1
print (f"The circle area is {circle_2}")

class Perimeter(Area):
    def __init__(self, pie, r):
        super().__init__(pie, r)
pie_3 = 3.1416
r2 = int(input("Enter a number : "))
perimeter1 = Perimeter(pie_3, r2)
perimeter2 = 2* pie_3 * r2
print (f"The perimeter area is {perimeter2}")