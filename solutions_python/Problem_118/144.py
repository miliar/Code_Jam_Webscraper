def base(n,b):
    if (n < b): return [n]
    else:
        l = base(n/b, b)
        l.append(n%b)
        return l

################################################################
def palindrome(x):
    s = str(x)
    n = len(s)
    for i in range(n/2):
        if s[i] != s[n-i-1]:
            return False
    return True

def to_int(l):
    return int("".join([str(i) for i in l]))

def fair_squares_to_len(n):
    l = ["", "0", "1", "2"]
    r = [0, 1, 4, 9]
    def check(s):
        i = to_int(s)
        if palindrome(i*i) and len(str(i*i)) <= 2*n:
            l.append(s)
            r.append(i*i)
    while l:
        a = l.pop()
        for i in range(0, (n-len(a))):
            z = str(0)*i
            check ("1"+z+a+z+"1")
            check ("2"+z+a+z+"2")
    return r

FAIRSQUARES = fair_squares_to_len(50)
FAIRSQUARES.sort()

def solve():
    low,high = [int(x) for x in input.readline().split(' ')]
    return len([i for i in FAIRSQUARES if low <= i <= high])

################################################################

from datetime import datetime
time_start = datetime.today()
def now(): return datetime.today() - time_start 

import sys
infilename = sys.argv[1]
outfilename = infilename.replace('.in','.out')

input = open(sys.argv[1], 'r')
output = open(sys.argv[1].replace('.in','.out'), 'w')
n = int(input.readline())

for i in range(1,n+1):
    result = solve()
    print "Case #%d: %s \t %s" % (i, result, now())
    output.write("Case #%d: %s\n" % (i, result))
    output.flush()
