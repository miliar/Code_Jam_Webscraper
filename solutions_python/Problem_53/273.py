import sys
T = input()
for t in range(T):
    sys.stdout.write('Case #%d: ' % (t + 1))
    N, K = map(int, raw_input().split())
    if K & (2 ** N - 1) == 2 ** N - 1:
        sys.stdout.write('ON\n')
    else:
        sys.stdout.write('OFF\n')
