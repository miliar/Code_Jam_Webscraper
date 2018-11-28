import sys
import gmpy
import math

def checkPalindrome(s):
    if len(s) < 1:
        return True
    else:
        if s[0] == s[-1]:
            return checkPalindrome(s[1:-1])
        else:
            return False


fh = open(sys.argv[1])
lines = fh.readlines()
fh.close()
lines = [x.strip() for x in lines]

numCases = int(lines[0])
results = []

for caseNum in range(numCases):
    foo = lines[caseNum+1].split()
    a = int(foo[0])
    b = int(foo[1])
    count = 0
    for i in range(a,b+1):
        if not gmpy.is_square(i):
            continue
        elif not checkPalindrome(str(i)):
            continue
        elif not checkPalindrome(str(int(math.sqrt(i)))):
            continue
        else:
            count += 1
    print "Case #" + str(caseNum+1) + ": " + str(count)
