t = int(input().strip())
for case in range(1, t + 1):
    s, k = input().split()
    k = int(k)
    s = list(map(lambda x: 0 if x == '+' else 1, s))
    flips = [0 for _ in s]
    cnt = 0
    parity = 0
    for i in range(len(s)):
        if parity != s[i]:
            if i < len(s) - k + 1:
                cnt += 1
                parity ^= 1
                flips[i + k - 1] ^= 1
            else:
                print('Case #{}: IMPOSSIBLE'.format(case))
                break
        parity ^= flips[i]
    else:
        print('Case #{}: {}'.format(case, cnt))
    
    
