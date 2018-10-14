import math

def palin(s):
    if s == s[::-1]:
        return True
    return False

f = open("inputcsmall.txt")
cases = int(f.readline())

for c1 in range(0,cases):
    line = f.readline().split(" ")
    a = long(line[0])
    b = long(line[1])
    n = long(math.sqrt(a))
    if n*n < a:
        n+=1
    numPalins = 0
    while n*n <= b:
        if(palin(str(n))):
            if(palin(str(n*n))):
                numPalins+=1
        n+=1
    print "Case #"+str(c1+1)+": "+str(numPalins)
