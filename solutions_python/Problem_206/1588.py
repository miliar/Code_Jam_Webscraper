import sys
sys.setrecursionlimit(1000000)

def function(D, K):
    # K = [[position, speed], ...] sorted by increasing position
    N = len(K)
    if N == 1:
        return K[0]
    elif N == 2:
        x1, x2 = K[0][0], K[1][0]
        v1, v2 = K[0][1], K[1][1] 
        if (D - x1) / v1 <= (D - x2) / v2:
            return K[1]
        else:
            return K[0]
    else:
        new_K = [K[0]]
        x = function(D, K[1:])
        new_K.append(x)
        return function(D, new_K)


T = int(raw_input().strip())  # read a line with a single integer

for i in xrange(1, T + 1):
    D, N = map(int, raw_input().strip().split(' '))  # read input
    D = float(D)
    K = []
    for j in xrange(N):
        K.append(map(float, raw_input().strip().split(' ')))
    K = sorted(K, key=lambda x:x[0], reverse=False)
    x, v = function(D, K)
    speed = v * D / (D - x)
    print "Case #{:d}: {:.6f}".format(i, speed)
