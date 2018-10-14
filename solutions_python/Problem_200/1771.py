def solve():
    t = int(raw_input())
    for i in range(t):
        n = raw_input()
        start = 0
        correct = True
        for j in range(1, len(n)):
            if n[j - 1] > n[j]:
                correct = False
                break
            if n[j - 1] != n[j]:
                start = j
        if not correct and start < len(n) - 1:
            n = int(n[:start] + str(int(n[start]) - 1) + '9' * (len(n) - start - 1))

        print 'Case #{}: {}'.format(i + 1, n)


solve()
