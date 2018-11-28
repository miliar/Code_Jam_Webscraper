# oversize pancake flipper
# code jam - qualification round - 2017
# uses python 3

T = int(input().strip())    # number of cases

for t in range(1,T+1):
    seq, K = input().strip().split()
    K = int(K)
    N = len(seq)
    seq = [1 if c=='+' else 0for c in seq]

    flips = 0   # number of flips
    possible = True # possibility flag
    j = 0   # position of last unhappy pancake
    
    while True:
        try:
            diff = seq[j:].index(0)
        except ValueError:
            break
        j += diff    
        if j>N-K:
            possible = False
            break
        flips += 1
        for jj in range(j,j+K):
            seq[jj] ^= 1

    if possible:
        print('Case #{}: {}'.format(t, flips))
    else:
        print('Case #{}: IMPOSSIBLE'.format(t))    