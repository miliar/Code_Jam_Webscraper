def readinput(inputname):
    f = open(inputname, 'r')
    n = int(f.readline()[0:-1])
    c = []
    for i in range(n):
        c.append(readcase(f))
    f.close()
    return c

def readcase(f):
    t = int(f.readline()[0:-1])
    temp = f.readline().split()
    na = int(temp[0])
    nb = int(temp[1])
    c = {'t':t, 'na':na, 'nb':nb, 'la':[], 'lb':[], 'aa':[], 'ab':[]}
    for i in range(na):
        temp = f.readline().split()
        c['la'].append(int(temp[0][0:2])*60 + int(temp[0][3:5]))
        c['ab'].append(int(temp[1][0:2])*60 + int(temp[1][3:5]) + t)
    c['la'].sort()
    c['ab'].sort()
    for i in range(nb):
        temp = f.readline().split()
        c['lb'].append(int(temp[0][0:2])*60 + int(temp[0][3:5]))
        c['aa'].append(int(temp[1][0:2])*60 + int(temp[1][3:5]) + t)
    c['lb'].sort()
    c['aa'].sort()
    return c

def solvecase(c):
    la = []
    la.extend(c['la'])
    lb = []
    lb.extend(c['lb'])
    aa = []
    aa.extend(c['aa'])
    ab = []
    ab.extend(c['ab'])
    
    a = 0
    b = 0
    
    for i in range(c['na']):
        if len(aa) > 0:
            if la[i] >= aa[0]:
                aa = aa[1:]
            else:
                a += 1
        else:
            a += 1
            
    for i in range(c['nb']):
        if len(ab) > 0:
            if lb[i] >= ab[0]:
                ab = ab[1:]
            else:
                b += 1
        else:
            b += 1
        
    return {'a':a,'b':b}
        
def solve(inputfile, outputfile):
    c = readinput(inputfile)
    o = open(outputfile, 'w')
    for i in range(len(c)):
        x = solvecase(c[i])
        o.write('Case #'+`i+1`+': '+`x['a']`+' '+`x['b']`+'\n')
    o.close()

solve('./B-large.in', './B-large.out')
