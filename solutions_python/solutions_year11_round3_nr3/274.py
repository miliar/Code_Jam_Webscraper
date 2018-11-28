import re,sys
numCases = int(sys.stdin.readline())
cases = []

def divides(n,f):
    out = True
    for freq in f:
        if freq % n != 0 and n % freq != 0:
            out = False
    return out

def result(n,l,h,freqs):
    for num in range(l,h+1):
        if divides(num,freqs):
            return str(num)
    return "NO"

for n in range(numCases):
    f = map(int,re.split(r'\s+',sys.stdin.readline().strip()))
    N = f[0]
    L = f[1]
    H = f[2]
    freqs = map(int,re.split(r'\s+',sys.stdin.readline().strip()))
    cases.append([N,L,H,freqs])

i = 1
for case in cases:
    print "Case #" + str(i) + ": " + result(case[0],case[1],case[2],case[3])
    i = i + 1
