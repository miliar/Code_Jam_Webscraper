def make_tidy(n):
    index = -1
    for i in xrange(len(n)-1):
        if n[i] > n[i+1]:
            index = i
            break
    if index != -1:
        l = len(n[index+1:])
        i = index
        if n[i] == 1:
            while i >= 0 and n[i] == 1:
                n[i+1] = 9
                n[i] = 0
                i -= 1
                # print 'n:', n
            n = n[:index+2] + [9] * (l-1)
        else:
            i = index
            while i >= 0 and n[i] > n[i+1]:
                n[i+1] = 9
                n[i] -= 1
                i -= 1
                # print 'n:', n
            n = n[:index+2] + [9] * (l-1)
    return n


t = int(raw_input())

for i in xrange(t):
    n = list(map(int, list(raw_input())))
    tidy = make_tidy(n)
    tidy = ''.join(str(x) for x in tidy)
    tidy = tidy.lstrip('0')
    print 'Case #%d: %s' % (i+1, tidy)
