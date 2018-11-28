import Solve
from math import ceil, sqrt

def fair_square(args):
    nmin, nmax = args[0].split(" ")
    nmax = float(nmax)
    nmin = float(nmin)
    i = int(ceil(sqrt(nmin)))
    square = i * i
    count = 0
    while square <= nmax:
        if str(i) == str(i)[::-1] and str(square) == str(square)[::-1]:
            count +=1
        i += 1
        square = i * i
    return str(count)

if __name__ == "__main__":
    Solve.solve("C-small-attempt1.in", "C.txt", fair_square, 1)
