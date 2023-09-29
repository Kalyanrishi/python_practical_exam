class Rectangle():
    def __init__(self, breadth, length):
        self.length = length
        self.breadth = breadth
    
    def area(self):
        return self.length * self.breadth
    a = int(input("Enter length of rectangle: "))
    b = int(input("Enter the breadth of rectangle: "))