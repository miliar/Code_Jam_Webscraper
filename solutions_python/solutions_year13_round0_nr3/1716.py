import sys
import re
import math



def isPal(s):
    return s == s[::-1]


def isSquare(i):
    s = int(math.sqrt(i))
    if not isPal(str(s)):
        return False
    return i == s**2


def main():
    f = open('C-small-attempt0.in', 'r')
    output = open('C-small-attempt0.out', 'w')
    text = f.read()
    f.close()
    lines = re.split("[\n|\r]",text)
    T = int(lines[0])
    i = 1
    
    for n in range(1,T+1):
        dims = lines[i].split(' ')
        i += 1
        A = int(dims[0])
        B = int(dims[1])

        c=0
        for z in range(A, B+1):
            if isPal(str(z)) and isSquare(z):
                c += 1  
        output.write('Case #' + str(n) + ': ' + str(c) +'\n')
            
    output.close()

    

if __name__ == '__main__':
    main()
