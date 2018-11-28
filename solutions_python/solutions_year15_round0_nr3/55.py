def mult(a, b):
    c = ''
    if (a[0] == '-') ^ (b[0] == '-'): c += '-'
    a = a[-1]
    b = b[-1]
    if (a == '1'): c += b
    elif (b == '1'): c += a
    if (a == b and a != '1'): c += '-1'
    if (a == 'i' and b == 'j'): c += 'k'
    if (a == 'j' and b == 'i'): c += '-k'
    if (a == 'j' and b == 'k'): c += 'i'
    if (a == 'k' and b == 'j'): c += '-i'
    if (a == 'k' and b == 'i'): c += 'j'
    if (a == 'i' and b == 'k'): c += '-j'
    if c[:2] == '--': c = c[2:]
    return c

T = input()
for t in range(1, T + 1):
    print "Case #%d:" % t,
    L, X = map(int, raw_input().split())
    s = raw_input()
    lprod = reduce(mult, s, '1')
    lxprod = '1'
    if L == 1:
        print "NO"
        continue
    for i in range(X % 4):
        lxprod = mult(lxprod, lprod)
    if lxprod != '-1':
        print "NO"
        continue
    s *= 4
    left = '1'
    i = 0
    while i < L * 4:
        left = mult(left, s[i])
        if left == 'i': break
        i += 1
    right = '1'
    j = -1
    while j >= -L * 4:
        right = mult(s[j], right)
        if right == 'k': break
        j -= 1
    #print i, L * X + j,
    if i >= L * X + j:
        print "NO"
        continue
    print "YES"
