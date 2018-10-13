
def merge(l, k, v):
    if k == 0: return
    for (i, (lk, lv)) in enumerate(l):
        if lk == k:
            l[i] = (lk, lv+v)
            break
    else:
        l.append((k, v))
    

t = int(raw_input())
for a in xrange(t):
    n, k = [int(_) for _ in raw_input().replace('\r', '').split(' ')]
    spans = [(n, 1)]
    while True:
        new_spans = []
        for l, num in spans:
            if k <= num:
                res = (l/2, (l-1)/2)
                break
            else:
                k -= num
                merge(new_spans, l/2, num)
                merge(new_spans, (l-1)/2, num)
        else:
            spans = new_spans
            continue
        break
    print 'Case #%d: %d %d' % (a+1, res[0], res[1])