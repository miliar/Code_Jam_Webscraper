#!/usr/bin/python2

f = open('C-small-attempt0.in')
tc = int(f.readline().strip())

for t in range(tc):
    a, b = f.readline().strip().split()
    a = int(a)
    b = int(b)
    pairs = set()
    count = 0 
    print "Case #%d: " % (t + 1),
    
    for n in range(a, b):
        strn = str(n)
        for i in range(len(strn) - 1):
            strn = strn[-1] + strn[:-1]
            m = int(strn)
            if m > n and m <= b:
                if (n, m) not in pairs:
                    count += 1
                    pairs.add((n, m))
                # cannot use break here!
                # one n can correspond to many m!
    print count
