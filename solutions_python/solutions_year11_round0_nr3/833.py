#!/usr/bin/python

def solve(l):
    m = -1
    for bitmask in range(1, 2**len(l)-1):

        xora = 0
        xorb = 0
        suma = 0
        sumb = 0
        for pos in range(len(l)):
            if bitmask & (1<<pos):
                xora = xora ^ l[pos]
                suma = suma + l[pos]
            else:
                xorb = xorb ^ l[pos]
                sumb = sumb + l[pos]
        if (xora == xorb):
            m = max(m, suma, sumb)
    return None if m < 0 else m                    

n = int(raw_input())
for i in range(n):
    k = int(raw_input())
    l = map(int, raw_input().split())
    res = solve(l)
    print "Case #%s: %s" % (i+1, res if res != None else "NO")

