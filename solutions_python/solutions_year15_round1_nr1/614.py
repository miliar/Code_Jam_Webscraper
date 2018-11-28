__author__ = 'emorfin'
import sys
import time

__author__ = 'emorfin'
import sys
import time

def method1(m):
    m1 = m[0:len(m)-1]
    m2 = m[1:len(m)]
    print m1
    print m2
    i = 0
    m3 = range(0,len(m1))
    while i < len(m1):
        m3[i] = int(m1[i]) - int(m2[i])
        if m3[i] < 0:
            m3[i] = 0
        i += 1
    print m3
    return sum(m3)

def method2(m):
    deltas = [max(int(x)-int(y), 0) for (x,y) in zip(m[:-1],m[1:])]
    print deltas
    rate = max(deltas)
    eats = 0
    for mm in m[:-1]:
        eaten = min([rate, mm])
        eats += eaten
    return eats

fin = open(sys.argv[1])
output_filename = sys.argv[1].replace('.in', '-a-' + str(int(time.time())) + '.out')
fout = open(output_filename, 'w')  #unwise

T = int(fin.readline())

for t in range(T):
    print "Test Case #", t+1
    N = fin.readline()
    print " N =", N
    m_set = [int(x) for x in fin.readline().split()]

    print " m_i =", m_set

    result1 = method1(m_set)

    result2 = method2(m_set)

    outstr = "Case #" + str(t + 1) + ': ' + str(result1) + ' ' + str(result2) + "\n"
    sys.stdout.write(" - " + outstr)
    fout.write(outstr)
