#!python3
import math

f = open("C-small-attempt0.in", 'r')
g = open("out-C-small.txt", 'w')

stuff = f.read()
f.close()

L = stuff.split("\n")
cases = int(L.pop(0))

def isPalin(s):
    for i in range(len(s)//2):
        if s[i] != s[-(i+1)]:
            return False
    return True

def isSquare(i):
    root = math.sqrt(i)
    if int(root + 0.5) ** 2 == i: 
        return True
    else:
        return False

for case in range(cases):
    
    count = 0
    pie = L.pop(0).split(" ")
    start = pie[0]
    end = pie[1]

    for i in range(int(start), int(end)+1, 1):
        if isSquare(i):
            if isPalin(str(i)) and isPalin(str(int(math.sqrt(i)))):
                count += 1

    g.write("Case #{}: {}\n".format(case+1, count))
g.close()
