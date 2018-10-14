def test(name, n, nCase):
    vowels = 'a e i o u'.split(' ')
    l = len(name)
    ans = 0
    for i in range(l):
        for j in range(1, l+1):
            c = 0
            if j - i < n:
                continue
            for k in range(i, j):
                if name[k] not in vowels:
                    c += 1
                    if c >=n:
                        break
                else:
                    c = 0
            if c >= n:
                ans += 1
    print 'Case #' + str(nCase) + ':', ans

if __name__ == '__main__':
    t = int(raw_input())
    for i in range(t):
        line = raw_input().split(' ')
        name, n = line[0], int(line[1])
    	test(name, n, i + 1)

