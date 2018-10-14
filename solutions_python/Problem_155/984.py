for t in range(1, int(input()) + 1):
    s, a = input().split()
    v, n = 0, 0
    for sh, ai in enumerate(map(int, a)):
        if n < sh:
            v, n = v + sh - n, sh
        n += ai        
    print('Case #', t, ': ', v, sep='')
