class PrintString():
    def __init__(self):
        self.string = " "

    def get(self):
        self.string = input("Enter the string: ")

    def put(self):
        print("The printed string is:", self.string)

obj = PrintString()  # Corrected the class name to PrintString
obj.get()
obj.put()