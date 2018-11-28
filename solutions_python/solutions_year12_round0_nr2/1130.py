import sys
import string

# Arguments: [in] [out]
# Defaults: in='input.txt', out=stdout

if len(sys.argv) > 1:
    input_file = len(sys.argv)>1 and sys.argv[1] or 'input.txt'
    outf = len(sys.argv)>2 and open(sys.argv[2],'w') or sys.stdout
    with open(input_file) as f:
        T = int(f.readline())
        for x in range(T):
            P = map(int, f.readline().split(' '))
            N = P[0] # dancers
            S = P[1] # surprises
            p = P[2] # min best result to count
            r = P[3:] # results
            count = 0
            for t in r:
                if t >= 3*p-2:
                    count = count + 1
                elif p > 1 and t >= 3*p-4 and S > 0:
                    count = count + 1
                    S = S - 1
            outf.write('Case #{0}: '.format(x+1))
            outf.write(str(count))
            outf.write('\n')
