class Circle():
    def __init__(self,pie,r):
        self.pie = pie
        self.r = r
pie_1 = 3.1416
r1 = int(input("Enter a number : "))
area = Circle(pie_1, r1)
area_2 = pie_1 * r1 * r1
print(area_2) 
    