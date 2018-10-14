# Imports

# Constants
DEBUG = True

f_name = 'A-large.in'#'test.in'#'A-small-attempt0.in'#
f2_name = 'A.out'


with open(f_name) as f:
    with open(f2_name,'w') as f2:
        T = int(f.readline()) # Discard first line
        for i in range(1, T+1):
            result = ''
            # Do the processing of each line
            D, N = f.readline().split()
            D = int(D)
            N = int(N)
            time = 0
            for j in range(N):
                K, S = f.readline().split()
                K = int(K)
                S = int(S)
                time = max((D - K)/S, time)
            result = D/time
            # Print this line
            print("Case #{}: {}".format(i, result), file=f2)

if DEBUG:
    with open(f2_name) as f2:
        for line in f2:
            print(line, end='')