import sys
import re

fin = open(sys.argv[1], 'r')
fout = open(re.sub(r'\.\w+$', '.out', sys.argv[1]), 'w')

def out(case, s):
    output = 'Case #' + str(case+1) + ': ' + str(s)
    fout.write(output + '\n')
    print output
    
def mapfloat(s):
    return map(float, s.split(' '))

for T in xrange(int(fin.readline())):
    c, f, x = mapfloat(fin.readline())
    
    seconds = 0.0
    cps = 2.0

    # how long until hit x at rate of cps
    base = x / cps
    
    def secsToNext(cps, c):
        return c / cps

    # get a farm, took 'seconds' amount of time
    seconds += secsToNext(cps, c)
    cps += f
    
    # total time is x / cps + seconds
    time = x / cps + seconds
    
    while time < base:
        base = time
        seconds += secsToNext(cps, c)
        cps += f
        time = x / cps + seconds
    out(T, base)
    
fout.close()