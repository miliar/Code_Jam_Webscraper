inputFileName = "C-small-attempt0.in"
outputFileName = "C-small-attempt0.out"

import math

class Vector :
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)
    def __repr__(self):
        return '(%d, %d)' % (self.x, self.y)
    def __str__(self):
        return '(%d, %d)' % (self.x, self.y)
    def __abs__(self):
        return math.sqrt(self.x**2 + self.y**2)
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y :
            return True
        return False
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    def angle(self):
        if self.x == 0:
            return math.pi / 2
        return math.atan(self.y/self.x)

def foo(R, x1, y1) :
    x2 = R * math.cos(math.asin(y1 / R))
    y3 = R * math.sin(math.acos(x1 / R))
    p2 = Vector(x2, y1)
    p3 = Vector(x1, y3)
    angle = (p3.angle() - p2.angle())
    area = math.pi * R**2 * angle / (2*math.pi)
    area -= R**2 * math.sin(angle) / 2
    area += (x2 - x1) * (y3 - y1) / 2
    return area

def solveCase(fileIn):
    f, R, t, r, g = [float(x) for x in fileIn.readline().split()]
    noHit = 0
    R_prime = R - t - f
    S = g + 2*r
    s = g - 2*f
    n = int(math.ceil(R / S))
    for i in range(n) :
        for j in range(n) :
            p1 = Vector(S*i + r + f, S*j + r + f)
            p2 = p1 + Vector(s, 0)
            p3 = p1 + Vector(0, s)
            p4 = p1 + Vector(s, s)
            if abs(p1) >= R_prime :
                pass
            elif abs(p4) <= R_prime :
                noHit += (g - 2*f)**2
            else :
                noHit += foo(R_prime, p1.x, p1.y)
                if abs(p2) < R_prime :
                    noHit -= foo(R_prime, p2.x, p2.y)
                if abs(p3) < R_prime :
                    noHit -= foo(R_prime, p3.x, p3.y)
    noHit *= 4
    total = math.pi * R**2
    p = (total - noHit) / total
    return str("%.6f" % p)

def main() :
    import sys
    fileIn = open(inputFileName)
    if outputFileName == "stdout" :
        fileOut = sys.stdout
    else :
        fileOut = open(outputFileName, "w")
    N = int(fileIn.readline())
    for i in range(N) :
        fileOut.write("Case #%d: " % (i+1))
        fileOut.write(solveCase(fileIn))
        fileOut.write("\n")
    fileIn.close()
    if outputFileName != "stdout":
        fileOut.close()

if __name__== "__main__" :
    main()
