# Imports

# Constants
DEBUG = True

f_name = 'C-small-1-attempt0.in'#'C-large.in'#'test.in'#
f2_name = 'C.out'


with open(f_name) as f:
    with open(f2_name,'w') as f2:
        T = int(f.readline()) # Discard first line
        for i in range(1, T+1):
            result = ''
            # Do the processing of each line
            N, K = f.readline().split()
            N = int(N)
            K = int(K)
            U = f.readline()
            U = float(U)
            P = list(map(float, f.readline().split()))
            probok = 1

            unit = 0.0001

            while(U > 0):
                current = P.index(min(P))
                #print(P)
                P[current] = round(P[current] + unit, 4)
                U = round(U-unit, 4)

            for j in range(N):
                probok *= P[j]

            result = '{0:.9f}'.format(probok)
            # Print this line
            print("Case #{}: {}".format(i, result), file=f2)

if DEBUG:
    with open(f2_name) as f2:
        for line in f2:
            print(line, end='')