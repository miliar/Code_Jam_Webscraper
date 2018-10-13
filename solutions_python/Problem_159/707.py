import sys
import string

# Arguments: [in] [out]
# Defaults: in='input.txt', out=stdout

if len(sys.argv) > 1:
    input_file = len(sys.argv)>1 and sys.argv[1] or 'input.txt'
    outf = len(sys.argv)>2 and open(sys.argv[2],'w') or sys.stdout
    with open(input_file) as f:
        T = int(f.readline())
        for tnr in range(T):
            N = int(f.readline())
            P = map(int, f.readline().split(' '))
            c1 = 0
            c2 = 0
            pr = P[0]
            for x in P[1:]:
                if x<pr:
                    c1 += pr-x
                pr =x
            pr = P[0]
            r =0
            for x in P[1:]:
                if x<pr:
                    if pr-x > r:
                        r=pr-x
                pr = x
            for x in P[:-1]:
                if x<r:
                    c2 += x
                else:
                    c2 += r
           
                
           
           
            outf.write('Case #{0}: '.format(tnr+1))
           
            outf.write('{0} {1}'.format(c1,c2))
            outf.write('\n')
