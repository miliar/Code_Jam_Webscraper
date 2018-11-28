import math
def read_ints():
    a = raw_input().split()
    return [int(x) for x in a]

def read_int():
    return read_ints()[0]

def solve():
    vals = read_ints()
    N, S, P = vals[0:3]
    T = [0] + vals[3:]
    
    B = []
    for y in range(S+1):
        B.append([0]*(N+1))
    for n in range(1, N+1):
        for s in range(S+1):
            B[s][n] = B[s][n-1]
            can_surprise = T[n] >= 2 and T[n] <= 28 and s > 0
            val = math.floor(T[n] / 3)
            if T[n] % 3 == 0:
                if T[n] / 3 >= P:
                    B[s][n] = max(B[s][n], 1+B[s][n-1])
                if can_surprise and (T[n] / 3) + 1 >= P:
                    B[s][n] = max(B[s][n], 1+B[s-1][n-1])
            elif T[n] % 3 == 1:
                if val + 1 >= P:
                    B[s][n] = max(B[s][n], 1+B[s][n-1])
                if can_surprise and val + 1 >= P:
                    B[s][n] = max(B[s][n], 1+B[s-1][n-1])
            elif T[n] % 3 == 2:
                if val + 1 >= P:
                    B[s][n] = max(B[s][n], 1+B[s][n-1])
                if can_surprise and val + 2 >= P:
                    B[s][n] = max(B[s][n], 1+B[s-1][n-1])
    """
    import pprint
    if N == S:
        print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
        for b in B:
            pprint.pprint(b)
        print '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
    """
    return B[S][N]

if __name__ == '__main__':
    T = read_int()
    for i in range(T):
        print 'Case #%d: %s' % (i+1, solve())
