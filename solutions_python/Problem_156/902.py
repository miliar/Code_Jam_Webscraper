ncase = int(raw_input())
for i in range(0, ncase):
    n = int(raw_input())
    lst = map(int, raw_input().split(' '))
    r = max(lst)
    reclst = []
    for j in range(2, r+1):
        tmp = 0
        tmp_lst = [obj for obj in lst]
        while True:
            m = max(tmp_lst)
            if m <= j:
                break
            tmp_lst[tmp_lst.index(m)] = m - j
            tmp_lst.append(j)
            tmp += 1
        tmp += j
        reclst.append(tmp)
    rec = 0
    if reclst:
        rec = min(reclst)
    else:
        rec = max(lst)
    print 'Case #%s: %s' % (i+1, rec)