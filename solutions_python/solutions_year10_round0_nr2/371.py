##!/usr/bin/python

#ifname = 'd:\\tmp\\test.txt'
#ofname = 'd:\\tmp\\test.out'

#ifname = 'd:\\tmp\\B-small.in'
#ofname = 'd:\\tmp\\B-small.out'

ifname = 'd:\\tmp\\B-large.in'
ofname = 'd:\\tmp\\B-large.out'


# redirect stdin and stdout
import sys
infile = open(ifname, 'r')
sys.stdout = open(ofname, 'w')

# the function to process a single case
import fractions
def findtime(N, t):
    T = 0
    for i in range (0, N-1):
        T = fractions.gcd(T, t[i]-t[i+1])
    T = abs(T)
    r = t[1]%T
    if (r==0):
        return 0
    else:
        return T-r 

# start the processing
C = 0
N = 0
line = infile.readline()
s = line.split()
C = int(s[0])
for k in range (0, C):
    line = infile.readline()
    s = line.split()
    N = int(s[0])
    t = s[1:N+1]
    for i in range (0, N):
        t[i] = int(t[i])
    result = findtime(N, t)
    print("Case #%d: "%(k+1), result)

infile.close()
