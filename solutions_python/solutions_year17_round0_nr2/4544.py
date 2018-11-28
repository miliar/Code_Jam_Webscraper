T = int(raw_input())

def tidy(v):
    a = map(int, list(str(v)))
    n = len(a)
    for i in range(n - 1):
        if a[i] <= a[i + 1]:
            pass
        else:
            return False
    return True

for tn in range(1, T + 1):
    n = int(raw_input())
    i = n
    while i >= 1:
        if tidy(i):
            print 'Case #%d: %d' % (tn, i)
            break
        i -= 1

