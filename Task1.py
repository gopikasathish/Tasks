from math import sqrt

class Vector:
    
    def __init__(self, x, y,z):
        self.x = x
        self.y = y
        self.z = z
        

    def __add__(self, other):
        if isinstance(other,Vector):
            return f'The sum of v0 and v1 is : ({self.x + other.x}, {self.y + other.y}, {self.z + other.z})'
        else:
            print("No result")

    def __sub__(self, other):
        if isinstance(other,Vector):
            return f'The difference of v0 and v1 is : ({other.x - self.x}, {other.y - self.y}, {other.z - self.z})'
        else:
            print("No result")

    
    def Dot(self,other):
    	
    		return f'The Dot product of v0 and v1 is :{self.x * other.x + self.y * other.y + self.z * other.z}'

    
    def sq(self): 
  
        return sqrt(self.x**2 + self.y**2 + self.z**2)
   


v0 = Vector(1,2,3)
v1 = Vector(5,6,7)
print(v0+v1)
print(v0-v1)
print(v0.Dot(v1))
print("The abs(v0) is :",abs(v0.sq()))



