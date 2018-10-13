tc = int(input())
for t in range(tc):
    n = list(map(int, list(input())))

    i = len(n)-1
    while i > 0:
        if n[i] < n[i-1]:
            for x in range(i, len(n)):
                n[x] = 9
            n[i-1] -= 1
        i -= 1

    print('Case #'+str(t+1) + ': ' + str(int(''.join(map(str, n)))))
