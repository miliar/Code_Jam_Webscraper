import math
import sys
eps = 1e-6

def isPal(s):
    return s==s[::-1]    

def isSquare(n):
    n = math.sqrt(n)
    if n-math.floor(n) < eps:
        return True
    return False
    
#print isSquare(5)
#print isSquare(25)
#print isSquare(100)
#print isSquare(101)

tc = input()
case = 1
while tc > 0:
    a, b = raw_input().split()
    a, b = int(a), int(b)
    
    cnt = 0
    st = int(math.sqrt(a))
    while st*st <= b:
        if st*st >= a and isSquare(st*st) and isPal(str(st*st)) and isPal(str(st)):
            #print st*st
            cnt += 1    
        st += 1
    
    sys.stdout.write("Case #" + str(case) + ": " + str(cnt) + "\n")
    case += 1
    tc -= 1
