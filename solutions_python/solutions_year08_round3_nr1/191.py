def readinput(inputname):
    f = open(inputname, 'r')
    n = int(f.readline()[0:-1])
    c = []
    for i in range(n):
        c.append(readcase(f))
    f.close()
    return c

def readcase(f):
    temp = f.readline().split()
    c = {'P':int(temp[0]), 'K':int(temp[1]), 'L':int(temp[2]), 'F':[]}
    temp = f.readline().split()
    i = 0
    for x in temp:
        y = int(x)
##        if c['F'].has_key(y):
##            c['F'][y].append(i)
##        else:
##            c['F'][y] = [i]
        c['F'].append(y)
        i+=1
    print c
    return c

def solvecase(c):
    k = []
    k.extend(c['F'])
    k.sort()
    k.reverse()

    l = []

    count = 0
    i = 1
    j = 0
    for x in k:
        count += i*x
        j+=1
        if j%c['K'] == 0:
            i+=1

    print "--"
        
    return count
        
def solve(inputfile, outputfile):
    c = readinput(inputfile)
    o = open(outputfile, 'w')
    for i in range(len(c)):
        x = solvecase(c[i])
        o.write('Case #'+`i+1`+': '+`x`+'\n')
    o.close()

solve('./A-small-attempt0.in', './A-small-attemp0.out')
