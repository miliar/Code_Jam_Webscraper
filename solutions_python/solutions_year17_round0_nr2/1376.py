with open('b.out', 'w') as f:
    m = int(input())
    for c in range(m):
        n = input()
        i = len(n) - 2
        while i >= 0:
            if n[i] > n[i + 1]:
                n = n[:i] + str(int(n[i]) - 1) + '9' * (len(n) - i - 1)
            i -= 1
        print('Case #{0}:'.format(c + 1), int(n), file=f)
