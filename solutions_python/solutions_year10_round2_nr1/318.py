# Has been a great while since I coded...Here Goes
# Snapper
# Usage pretty simple: Q1.py <inputfile>
# requires a EOF to terminate


#Read Input - Absolutely 0 input checks

import fileinput

    
infile = fileinput.input()

p = infile.readline()

T = long(p)

t = 0


while t < T:
    t += 1
    params = infile.readline()
    N,M = [long(p) for p in params.split()]
    root = {}
    
    for i in range(N):
        params = infile.readline()
        files = params.strip().split('/')
        dir = root
        for f in files:
            if len(f) <= 0:
                continue
            if not dir.has_key(f):
                dir[f] = {}
            dir = dir[f]

#    print root
    count = 0

    for j in range(M):
        params = infile.readline()
        files = params.strip().split('/')
        dir = root
        for f in files:
            if len(f) <= 0:
                continue
            if not dir.has_key(f):
                dir[f] = {}
#                print "Creating [", f, "]", len(f)
                count += 1
            dir = dir[f]

#    print root,count

    print 'Case #%d: %d' % (t, count)
            
infile.close()

