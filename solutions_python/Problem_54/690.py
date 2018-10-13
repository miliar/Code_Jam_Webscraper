# May, 8, 2010
# Qualification Round
# "Fair Warning"

from time import time
from math import sqrt

#inpath = "B-sample.in"
#inpath = "B-large.in"
inpath = 'B-small-attempt1.in'
outpath = "B.out"

def LCD(a, b):
    while b > 0:
        while a >= b:
            a -= b
        a, b = b, a
    return a

def Anniversary(events):
    some_event = events[0]
    events = list(abs(events[i] - events[i+1])
                  for i in range(len(events)-1))
    d = events[0]
    for e in events:
        d = LCD(d, e)
    if some_event%d == 0:
        return 0
    return d - (some_event%d)
    
timestart = time()

fin = open(inpath)
fout = open(outpath, 'w')

T = int(fin.readline())
for case in range(1, T+1):
    events = map(int, fin.readline().split())[1:]
    fout.write("Case #%d: %d\n" % (case, Anniversary(events)))

fin.close()
fout.close()
print "%.4f" % (time() - timestart)
