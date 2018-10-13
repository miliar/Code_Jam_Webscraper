t = int(raw_input())
for i in range(t):
    ans = 0
    cakes, k = raw_input().split()
    cakes = list(cakes)
    k = int(k)
    for j in range(len(cakes) - k + 1):
        if cakes[j] == '-':
            for l in range(k):
                if cakes[j + l] == '-':
                    cakes[j + l] = '+'
                else:
                    cakes[j + l] = '-'
            ans += 1
    if '-' in cakes:
        print 'Case #' + str(i + 1) + ': ' + 'IMPOSSIBLE'
    else:
        print 'Case #' + str(i + 1) + ': ' + str(ans)

