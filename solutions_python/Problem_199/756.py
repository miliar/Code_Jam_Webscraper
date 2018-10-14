
f = open('A-large.in', 'r').readlines()

N = int(f[0])

for t_case in xrange(1, N+1):
    # print('Processing test case #{}'.format(t_case))

    P, K = f[t_case].split(' ')
    K = int(K)
    P = list(P)

    ans = 0
    for j in xrange(len(P) - K + 1):
        # If the current pancake is not flipped, flip it and update the rest
        if P[j] != '+':
            ans += 1
            for k in xrange(K):
                P[j + k] = ('+' if (P[j+k] == '-') else '-')

    # Check to see if the pancakes are aligned
    # print P
    if '-' not in P:
        ret = ans
    else:
        ret = 'IMPOSSIBLE'
    print('Case #{}: {}'.format(t_case, ret))

