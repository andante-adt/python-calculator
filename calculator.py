class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):   
        return a - b            #fixed from "return b - a" to "return a - b"

    def multiply(self, a, b):  
        result = 0
        if b >= 0:
            for i in range(b):
                result = self.add(result, a)
            return result
        else:
            for i in range(abs(b)):
                result = self.subtract(result, a)
            return result

    def divide(self, a, b):
        if b == 0:
            return "Any numbers can't be divided by zero"
        result = 0
        abs_a, abs_b = abs(a), abs(b)
        while abs_a >= abs_b:
            abs_a = self.subtract(abs_a, abs_b)
            result += 1
        if (a < 0) != (b < 0):
            result = -result
        return result
    
    def modulo(self, a, b):
        negative = 0
        if b == 0:
            return "You can't divide any numbers with zero"
        if a < 0:
            a = abs(a)
            negative = 1
        if b < 0:
            b = abs(b)
            negative = 1
        while a >= b:
            a = a - b
        return -a if negative == 1 else a

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(10, 2))
    print("Example: modulo: ", calc.modulo(10, -3))
