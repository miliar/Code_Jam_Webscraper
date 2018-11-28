
import math

def isPalin(n):
    n = str(n)
    return n == n[::-1]

def getNumSquares(a, b):
    count = 0
    for n in range(a, b+1):
        if isPalin(n):
            sq = math.sqrt(n)
            if (sq % 1 == 0) and isPalin(int(sq)):
                count += 1

    return count

def main():
    filePath = "input/C-small-attempt0.in"
    file = open(str(filePath))    
    lines = file.read().split()

    T = int(lines[0])
    lines = lines[1:]

    for t in range(0, T):
        output = getNumSquares(int(lines[2*t]), int(lines[2*t+1]))
        print("Case #%s: %d" % (t+1, output))

main()
