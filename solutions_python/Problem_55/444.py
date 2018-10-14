# Has been a great while since I coded...Here Goes
# Roller Coaster
# Usage pretty simple: Q3.py <inputfile>
# requires a EOF to terminate


#Read Input - Absolutely 0 input checks

import fileinput

infile = fileinput.input()

params = infile.readline()
C = long(params)

c = 0

while c < C:
    c += 1
    E = 0
    params = infile.readline()
    #print params
    R,k,N = [long(p) for p in params.split()]

    r = 0
    w = []

    params = infile.readline()
    q = [long(p) for p in params.split()]
    sum = 0

    while r < R:
        r += 1
        sum = 0
        #print k,sum,q,sum+q[0]
        while k >= (sum + q[0]):
            i = q.pop(0)
            sum += i
            w.append(i)
            #print q
            if len(q) <= 0:
                break
        E += sum
        q.extend(w)
        w = []
        #print q,E
    print "Case #%d: %d" % (c,E)

infile.close()

