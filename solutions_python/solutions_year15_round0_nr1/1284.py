__author__ = 'emorfin'

import sys

if len(sys.argv) != 2:
    print "Input filename expected."
    sys.exit(2)

fin = open(sys.argv[1])
fout = open(sys.argv[1].replace('.in', '.out'), 'w') #unwise

T = int(fin.readline())

for x in range(T):
    [Smax_str, S_data_str] = fin.readline().split()
    Smax = int(Smax_str)
    #print Smax, S_data_str
    Adata = [int(S_data_str[i]) for i in range(Smax+1)]
    F = Q = R = 0
    for i in range(Smax + 1):
        R = i - Q
        if R > 0:
            F += R
            Q = i + Adata[i]
        else:
            Q += Adata[i]
    outstr =  'Case #' + str(x + 1) + ': ' + str(F) + '\n'
    fout.write(outstr)
fin.close()
fout.close()
