def nflips(i, k):
    maxshift = i.bit_length() - k
    mask = (1<<k)-1
    shift = n = 0
    while i:
        while not i>>shift & 1:
            shift += 1
            if shift > maxshift:
                return -1
        i ^= mask << shift
        n += 1
    return n

T = int(input())
for i in range(T):
    S, K = input().split()
    K = int(K)
    bits = sum((c == '-') << i for i, c in enumerate(S))
    flips = nflips(bits, K)
    out = flips if flips != -1 else 'IMPOSSIBLE'
    print('Case #%d: %s' % (i+1, out))
