import fractions

from decimal import *
getcontext().prec = 100

fin = open('inputA.txt')
fout = open('outputA.txt','w')
num_tests = int(fin.readline())

for test_num in range(1, num_tests + 1):
    line = fin.readline().split()
    reduced = line[0].split("/")
    P = int(reduced[0])
    Q = int(reduced[1])

    g = fractions.gcd(P,Q)
    P = P/g
    Q = Q/g

    j = 0
    B = Q
    while B % 2 == 0:
        B = B/2
        j += 1

    if j > 40 or B != 1:
        fout.write("Case #" + str(test_num) + ": impossible" + "\n")
    else:
        k = 0
        while P < Q:
            Q = Q/2
            k += 1
        fout.write("Case #" + str(test_num) + ": " + str(k) + "\n")
    
##    i = 0
##    A = P
##    C = Q
##    while A % 2 == 0:
##        A = A/2
##        C = C/2
##        i += 1
##
##    j = 0
##    B = Q
##    while B % 2 == 0:
##        B = B/2
##        j += 1
##
##    if j - i > 40 or A % B != 0:
##        fout.write("Case #" + str(test_num) + ": impossible" + "\n")
##    else:
##        k = i
##        while A < C:
##            C = C/2
##            k += 1
##        fout.write("Case #" + str(test_num) + ": " + str(k) + "\n")
        
    print test_num
    
fin.close()
fout.close()
