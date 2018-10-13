global mul
mul = {'11': '1', '1i': 'i' ,'1j': 'j', "1k": 'k',
      'i1': 'i', 'ii': '-1' ,'ij': 'k', "ik": '-j',
      'j1': 'j', 'ji': '-k' ,'jj': '-1', 'jk': 'i',
      'k1': 'k', 'ki': 'j' ,'kj': '-i', 'kk': '-1'}

def multi(x, y):
    neg = False
    if x[0] == '-':
        neg = True
        x = x[1]
    if y[0] == '-':
        neg = False if neg else True
        y = y[1]
    key = "%s%s" % (x, y)
    val = mul[key]
    if neg:
        if val[0] == '-':
            val = val[1]
        else:
            val = '-' + val
    return val

def check(string, L, X):
    mult = '1'
    g = X
    
    for s in range(X):
        for c in string:
            mult = multi(mult, c)
        if mult == "1":
            g = s+1
            break
    rest = X % g
    if mult != '-1':
        mult = '1'
        for c in (string * rest):
            mult = multi(mult, c)
        if mult != '-1':
            return "NO"
        if mult != '-1':
            return "NO"

    if_i = False
    if_k = False
    mult = '1'
    for c in (string * g * 2):
        mult = multi(mult, c)
        if mult == 'i':
            if_i = True
        if mult == 'k' and if_i:
            if_k = True

    if if_i and if_k:
        return "YES"
    else:
        return "NO"

cases = int(raw_input())
for case in range(cases):
    line1 = raw_input().split()
    L, X = map(int, line1)
    string = raw_input()
    leng = L*X
    if leng < 3:
        print "Case #%s: NO" % (case+1)
        continue
    print "Case #%s: %s" % (case+1, check(string, L, X))

