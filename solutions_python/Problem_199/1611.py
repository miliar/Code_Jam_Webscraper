T = int(input().split()[0])

for i in range(T):
    s = input().split()
    S = s[0]
    K = int(s[1])
    N = [-1 if x=='-' else 1 for x in S]
    c = 0
    for j in range(len(N)-K+1):
        if N[j] == -1:
            N[j:j+K] = [-x for x in N[j:j+K]]
            c += 1
        else:
            continue
    if sum(N) == len(N):
        print('Case #{0}: {1}'.format(i+1, c))
    else:
        print('Case #{0}: {1}'.format(i+1, 'IMPOSSIBLE'))
