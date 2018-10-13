import os
import sys
import math

def palin(x):
    s1 = str(x)

    s2 = ''
    for i in xrange(1,len(s1)+1):
        s2 += s1[-i]

    return (int(s1)==int(s2))

def precalc():
    VALUES = [1,2,3]
    
    val = 1
    while val <= 128:
        s_left = bin(val)[2:]
        
        s_right = ''
        i = len(s_left) - 1
        while i >= 0 :
            s_right += s_left[i]
            i -= 1
            
        vs = [s_left + s_right, s_left + '0' + s_right, s_left + '1' + s_right, s_left + '2' + s_right]

        s_left2 = '2' + s_left[1:]
        s_right2 = s_right[:-1] + '2'

        vs += [s_left2 + s_right2, s_left2 + '0' + s_right2, s_left2 + '1' + s_right2, s_left2 + '2' + s_right2]
        for s in vs:
            x = int(s)
            xx = x*x
            if palin(xx):
                #print '%d --> %s -- > %s' % (len(s), str(x), str(xx))
                VALUES.append(x)

        val += 1

    return VALUES

def main(f):
    # pre-calc
    mm = sorted(list(precalc()))
    pre = map(lambda x: x*x, mm)
    
    # solve
    inFile = open(f)
    
    T = int(inFile.readline())

    r = []
    for i in xrange(0, T):
        v = inFile.readline()
        [A,B] = map(lambda x: int(x), v.split(' '))

        res = 0
        for x in pre:
            if x >= A and x <= B:
                res += 1

        r.append(res)

    outFile = open(f.replace('.in', '.out'), 'w')
    for i in xrange(0, T):
        outFile.write('Case #%d: %d\n' % ((i+1), r[i]))
    outFile.close
    
if __name__ == '__main__':
    main('%s/%s' %(os.path.dirname(sys.argv[0]), 'C-large-1.in'))

