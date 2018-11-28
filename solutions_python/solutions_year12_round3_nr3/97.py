import copy

def trace(f):
    indent = '   '
    def _f(*args):
        signature = '%s(%s)' % (f.__name__, ', '.join(map(repr, args)))
        print '%s--> %s' % (trace.level*indent, signature)
        trace.level += 1
        try:
            result = f(*args)
            print '%s<-- %s == %s' % ((trace.level-1)*indent,
                                      signature, result)
        finally:
            trace.level -= 1
        return result
    trace.level = 0
    return _f


def processArray(aarr, barr, max, type):
    #print 'Trying', aarr, barr, max
    if not aarr:
        return max
    a1 = int(aarr.pop(0))
    A1 = int(aarr.pop(0))
    max1 = max
    max2 = max
    if (aarr and barr):
        #print 'TOSS', aarr, barr, max
        max1 = processArray(copy.deepcopy(aarr), copy.deepcopy(barr), copy.deepcopy(max1), 'TOSS')


    b1= -1
    B1 = -1
    while barr and B1 != A1:
        b1 = int(barr.pop(0))
        B1 = int(barr.pop(0))
    if B1 == A1 and a1 > b1 and b1>0:
        max2 += b1
        aarr.insert(0,A1)
        aarr.insert(0,a1-b1)
    elif B1 == A1 and b1 > a1:
        max2 += a1
        barr.insert(0,B1)
        barr.insert(0,b1-a1)
    elif a1 == b1 and B1 == A1 and b1>0:
        max2+= a1


    max2 = processArray(copy.deepcopy(aarr), copy.deepcopy(barr), copy.deepcopy(max2), 'KEEP')

    #print 'COMPARE', max1, max2
    if max2> max1:
        max1 = max2
    return copy.deepcopy(max1)





f = open('input', 'r')
fw = open('output', 'w')
len = f.readline()
#print len.rstrip()
i=0
for x in range(int(len)):
    i+=1
    line = f.readline()
    line = line.rstrip()
    x = line.split()
    N= int(x[0])  # min1
    M = int(x[1])
    #print N,M
    line = f.readline()
    line = line.rstrip()
    x = line.split()
    Narray = x
    #print Narray
    line = f.readline()
    line = line.rstrip()
    x = line.split()
    Marray = x
    #print Marray, 'END'
    max = 0
    #print 'START', Narray, Marray
    max = processArray(Narray, Marray, max, 'START')
    print 'Case #'+str(i)+': '+str(max)+'\n'
    fw.write( 'Case #'+str(i)+': '+str(max)+'\n')


