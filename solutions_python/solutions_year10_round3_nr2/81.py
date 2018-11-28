def findans(l, p, c):
    if l * c >= p:
        return 0
    if p <= l:
        return 0
    tp = p
    tpp = l
    while tpp < tp:
        tp = (tp + c - 1)/c
        tpp *= c
    return 1 + max(findans(tp, p, c ), findans(l, tpp, c))

fin = open('small.in')
fout = open('result.out', 'w')
data = fin.readlines()
for x in xrange(len(data)):
    data[x] = (data[x])[:-1]
cases = int(data[0])
for case in xrange(1, cases + 1):
    temp = data[case].split()
    l = int(temp[0])
    p = int(temp[1])
    c = int(temp[2])
    ans = findans(l, p, c)
    print >>fout, 'Case #' + str(case) + ':', str(ans)
fin.close()
fout.close()
