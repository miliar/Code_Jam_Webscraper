def readinput(inputname):
    f = open(inputname, 'r')
    n = int(f.readline()[0:-1])
    c = []
    for i in range(n):
        c.append(readcase(f))
    f.close()
    return c

def readcase(f):
    s = int(f.readline()[0:-1])
    c = {'s':[], 'q':[]}
    for i in range(s):
        c['s'].append(f.readline()[0:-1])
    q = int(f.readline()[0:-1])
    for i in range(q):
        c['q'].append(f.readline()[0:-1])
    return c

def solvecase(c):
    m = 0
    ms = '';
    for s in c['s']:
        x = c['q'].count(s)
        if x == 0:
            return 0
        x = c['q'].index(s)
        if x > m:
            m = x

    d = {'s':c['s'], 'q':c['q'][m:]}

    i = 1 + solvecase(d)
    return i
        
def solve(inputfile, outputfile):
    c = readinput(inputfile)
    o = open(outputfile, 'w')
    for i in range(len(c)):
        x = solvecase(c[i])
        o.write('Case #'+`i+1`+': '+`x`+'\n')
    o.close()

solve('./A-small-attempt2.in','./A-small-attempt2.out')

