from io import *
from math import *

def runFile(file):
    f = open(file)
    g = open("output" + file, 'w')
    num = int(f.readline().rstrip('\n'))
    for i in range(num):
        [r,t] = (f.readline().rstrip('\n').split(' '))
        r = int(r)
        t = int(t)
        c = 0
        a = Polynomial([2,-(1-2*r),-t])
        [x,y] = a.roots()
        x = int(x.real)
        g.write("Case #" + str(i+1) + ": " + str(x) + "\n")

class Polynomial:
    ## Intialize a polynomial with a list of coefficients.
    ## The coefficient list starts with the highest order term.
    def __init__(self, coeffs):
        self.order = len(coeffs)-1
        self.coeffs = coeffs

    ## Return the coefficient of the x**i term
    def coeff(self,i):
        if(i <= self.order):
            return self.coeffs[self.order-i]
        else:
            return None

    ## Return the value of this Polynomial evaluated at x=v
    def val(self, v):
        return sum([v**i * self.coeff(i) for i in range(len(self.coeffs))])

    ## Return the roots of this Polynomial
    def roots(self):
        det = (complex(self.coeffs[1],0)**2 - 4 * complex(self.coeffs[0],0) * complex(self.coeffs[2],0))**0.5
        return [(-complex(self.coeffs[1],0)+det)/(2*complex(self.coeffs[0],0)),(-complex(self.coeffs[1],0)-det)/(2*complex(self.coeffs[0],0))]
