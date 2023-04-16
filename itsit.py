class Math:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def subtract(self):
        return self.num1 - self.num2
    
    def divide(self):
        if self.num2 == 0:
            raise ValueError("Cannot divide by zero")
        return self.num1 / self.num2

def subtract(num1, num2):
    return num1 - num2

def divide(num1, num2):
    if num2 == 0:
        raise ValueError("Cannot divide by zero")
    return num1 / num2
math = Math(10, 5)
print(math.subtract()) 
print(math.divide()) 

print(subtract(10, 5)) 
print(divide(10, 5)) 