import sys
import math

class Memoize:
    def __init__(self, f):
        self.f = f
        self.memo = {}
    def __call__(self, *args):
        if not args in self.memo:
            self.memo[args] = self.f(*args)
        return self.memo[args]

def palindrome(x):
    
    temp = str(x)
    return temp == temp[::-1]
        

def createPosSquares(a,b):
    posSquares = []

    start = math.ceil(math.sqrt(a))
    if(start**2 > b):
        return []
    while(start**2 <= b):
        posSquares.append(int(start**2))
        start += 1
    return posSquares
    
f = open(sys.argv[1],"r")
output = open("fair_and_square.txt","w")
num = int(f.readline())
test_cases = f.read()
test_cases = test_cases.split("\n")
test_cases = test_cases[:-1]
for i in range(len(test_cases)):
    test_cases[i] = test_cases[i].split()
    for j in range(2):
        test_cases[i][j] = int(test_cases[i][j])


palindrome = Memoize(palindrome)
c = 0
for case in test_cases:
    c += 1
    fair = 0
    squares = createPosSquares(case[0],case[1])
    
    for i in squares:
        if(palindrome(int(math.sqrt(i)))):
            if palindrome(i):
                fair += 1


    output.write("Case #"+str(c)+": "+str(fair)+"\n")