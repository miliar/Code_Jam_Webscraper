def solve(N, K):
    """ solve the problem """

    layer = 1
    #while True:
    #    n = 2 ** (layer-1)
    #    if K > n:
    #        N -= n
    #        K -= n
    #    else:
    #        N -= n
    #        ans = int(N / n)
    #        if N % n != 0 and K <= (N % n): ans += 1
    #        return int((ans+1)/2), int(ans/2)
#
#        layer += 1
    while True:
        n = 2 ** (layer-1)
        if K > n:
            N -= n
            K -= n
        else:
            if N < n: return (0, 0)
            N -= n
            ans = int(N/n)
            if N % n != 0 and K <= (N % n): ans += 1
            return int((ans+1)/2), int(ans/2)
        layer += 1



def parse():
    """ parse input """

    N, K = input().split()
    N = int(N)
    K = int(K)

    return N, K


def main():
    
    T = int(input())

    # solve
    for t in range(1, T+1):
        params = parse()
        #if t != 4: continue
        result = solve(*params)
        print('Case #%d: %s %s' % (t, result[0], result[1]))


if __name__ == '__main__':

    main()
