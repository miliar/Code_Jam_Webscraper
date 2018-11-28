# https://code.google.com/codejam/contest/6224486/dashboard
import sys

def readline():
    return sys.stdin.readline().rstrip()

t = int(readline())
for x in range(t):
    line = readline()
    (n, s) = line.split()
    s = [int(y) for y in list(s)]
    #print 's = {}'.format(s)
    guests = 0
    level = 0
    for n in s:
        level = level + n - 1
        #print 'n = {}, level = {}'.format(n, level)
        if level < 0:
            guests = guests + (-level)
            #print 'guests = {}'.format(guests)
            level = 0
    result = guests
    print 'Case #{}: {}'.format(x+1, result)

