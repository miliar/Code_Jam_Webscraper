import numpy as np

f = open('A-small-attempt0.in', 'r')
r = int(f.readline())
for i in range(1,r+1):
    linenr = int(f.readline())
    for ln in range(1,5):
        l = np.fromstring(f.readline(), dtype=int, sep=' ')
        if ln == linenr:
            l1 = l
    linenr = int(f.readline())
    for ln in range(1,5):
        l = np.fromstring(f.readline(), dtype=int, sep=' ')
        if ln == linenr:
            l2 = l
    result = np.intersect1d(l1,l2)
    if len(result) == 1:
        print("Case #%i: %i" % (i,result[0]))
    elif len(result) == 0:
         print("Case #%i: Volunteer cheated!" % i)
    else:
        print("Case #%i: Bad magician!" % i)


