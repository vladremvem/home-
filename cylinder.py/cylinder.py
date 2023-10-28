import math
 
def Cylindra_v(r,h):
    #V = πr²h
    V= math.pi*pow (r,2)*h
    return V
def square_s(r,h):
    s= 2* math.pi* r* (r+h)
    return s
def surface(r,h):
    Q= 2 *math.pi*r*h
    return Q
r=int (input())
h=int ( input())
print("обем:",Cylindra_v(r,h))
print ("площя",square_s(r,h))
print("поверхня",surface(r,h))