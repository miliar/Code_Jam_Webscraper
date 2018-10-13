def test(a, b, nCase):
    n = 0
    fs = 0
    while True:
        n += 1
        rn = int(str(n)[::-1])
        if n == rn:
            n2 = n*n
            if n2 < a:
                continue
            if n2 > b:
                break
            rn2 = int(str(n2)[::-1])
            if n2 == rn2:
                fs += 1
    print 'Case #' + str(nCase) + ':', fs

if __name__ == '__main__':
    t = int(raw_input())
    for i in range(t):
        strLine = raw_input().split(' ')
        a, b = int(strLine[0]), int(strLine[1])
        test(a, b, i + 1)

