import sys

sys.stdin.readline()
for (cn, ln) in enumerate(sys.stdin.readlines(), 1):
    ln = list(map(int, list(ln.rstrip())))
    i = 0
    x = False
    while i+1 < len(ln):
        if ln[i+1] < ln[i]:
            q = ln[i]
            while i > 0 and ln[i-1] == q:
                i -= 1
            x = True
            break
        i += 1
    if x:
        ln[i] -= 1
        for j in range(i+1, len(ln)):
            ln[j] = 9
    n = ''.join(map(str, ln)).lstrip('0')
    if n == '': n = '0'
    print('Case #%s: %s' % (cn, n))
