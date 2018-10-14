for t in range(int(raw_input())):
    s = list(raw_input())
    n = len(s)

    good = False
    while not good:
        good = True
        for i in range(0, n - 1):
            if s[i] > s[i + 1]:
                good = False
                for j in range(i + 1, n):
                    s[j] = '0'
                break
        num = int(''.join(s))
        if good:
            print 'Case #%i: %i' % (t + 1, num)
        num = num if good else num - 1
        s = list(str(num))
        n = len(s)
