for case in range(int(input())):
    p, k = input().split()

    p = [1 if ch == '+' else -1 for ch in p]
    k = int(k)

    ct = 0
    for i in range(len(p)-k+1):
        if p[i] == -1:
            ct += 1
            for j in range(k):
                p[i+j] *= -1

    p = ''.join('+' if x == 1 else '-' for x in p)

    if p != len(p) * '+':
        ct = 'IMPOSSIBLE'

    print('Case #%d: %s' % (case+1, str(ct)))
