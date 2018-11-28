import sys

mul = {
    ('1', '1'): ('1', 1), # 1x1 = 1 (pos)
    ('1', 'i'): ('i', 1),
    ('1', 'j'): ('j', 1),
    ('1', 'k'): ('k', 1),
    ('i', '1'): ('i', 1),
    ('i', 'i'): ('1', -1),
    ('i', 'j'): ('k', 1),
    ('i', 'k'): ('j', -1),
    ('j', '1'): ('j', 1),
    ('j', 'i'): ('k', -1),
    ('j', 'j'): ('1', -1),
    ('j', 'k'): ('i', 1),
    ('k', '1'): ('k', 1),
    ('k', 'i'): ('j', 1),
    ('k', 'j'): ('i', -1),
    ('k', 'k'): ('1', -1)
}

def mult(l, r):
    out,sgn = mul[(l[0],r[0])]
    return (out, sgn*l[1]*r[1])

def power(i, power):
    sgn = i[1] if power % 2 == 1 else 1
    if i[0] == '1':
        out = '1'
    else:
        out = i[0] if power % 2 == 1 else '1'
        if (power/2) % 2 == 1:
            sgn *= -1
    return (out,sgn)

def evaluate(string):
    cur = '1'
    sgn = 1
    for c in string:
        ncur, nsgn = mul[(cur, c)]
        cur = ncur
        sgn *= nsgn
    return (cur, sgn)

T = int(sys.stdin.readline())

for i in range(T):
    L,X = map(int, sys.stdin.readline().split())
    string = (sys.stdin.readline().strip())
    assert len(string) == L
    # iCnt = 0
    # jCnt = 0
    # kCnt = 0
    # for c in string:
    #     if c == 'i':
    #         iCnt += 1
    #     elif c == 'j':
    #         jCnt += 1
    #     elif c == 'k':
    #         kCnt += 1
    #     else: assert False
    # iMod = iCnt % 2
    # jMod = jCnt % 2
    # kMod = kCnt % 2
    # if not (X % 2 == 0 or
    #         (iMod == 0 and jMod == 0 and kMod == 0) or
    #         (iMod == 1 and jMod == 1 and kMod == 1)):
    #     print "Case #%d: %s" % (i+1, "NO")
    #     continue
    # found = False
    total = evaluate(string)
    if (power(total,X) != ('1',-1)):
        # sc
        # print "Total fail", total, power(total,X)
        print "Case #%d: %s" % (i+1, "NO")
        continue
    cur = ('1',1)
    fsFound = False
    fsLoc = -1
    for q in range(1,6):
        addPow = mult(power(total,q),cur)
        # print "*",addPow
        if (addPow == ('i', 1) or addPow == ('i', -1)):
            fsFound = True
            fsLoc = L*q
            break
    if not fsFound:
        for j in range(1, L): # cut 1 (left-exclusive)
            first = mult(cur, (string[j-1],1))
            cur = first
            # print first
            if (first == ('i', 1) or first == ('i', -1)):
                fsFound = True
                if fsLoc == -1 or j < fsLoc:
                    fsLoc = j
                break
            for q in range(0,6):
                addPow = mult(power(total,q),cur)
                # print "*",addPow
                if (addPow == ('i', 1) or addPow == ('i', -1)):
                    fsFound = True
                    if fsLoc == -1 or L*q+j < fsLoc:
                        fsLoc = L*q+j
                    break
            # if fsFound: break
    if not fsFound:
        # print "First fail"
        print "Case #%d: %s" % (i+1, "NO")
        continue
    cur = ('1',1)
    tsFound = False
    tsLoc = -1
    for q in range(1,6):
        addPow = mult(cur,power(total,q))
        if (addPow == ('k', 1) or addPow == ('k', -1)):
            tsFound = True
            tsLoc = L*(X-q)
            break
    if not tsFound:
        for k in range(L-1, 0, -1):
            third = mult((string[k],1), cur)
            cur = third
            if (third == ('k', 1) or third == ('k', -1)):
                tsFound = True
                if tsLoc == -1 or L*(X-1)+k > tsLoc:
                    tsLoc = L*(X-1)+k
                break
            for q in range(0,6):
                addPow = mult(cur,power(total,q))
                if (addPow == ('k', 1) or addPow == ('k', -1)):
                    tsFound = True
                    if tsLoc == -1 or L*(X-q)+k > tsLoc:
                        tsLoc = L*(X-q)+k
                    break
    if not tsFound:
        # print "Third fail"
        print "Case #%d: %s" % (i+1, "NO")
        continue

    # found = False
    # for j,js in fs:
    #     for k,ks in ts:
    #         if k <= j: continue
    #         print j,k
    #         second = evaluate(string[j:k])
    #         if second[0] == 'j' and js*ks*second[1] == 1:
    #             found = True
    #             break
    #     if found: break

    if fsLoc >= tsLoc:
        # print "Diff fail",fsLoc,tsLoc
        print "Case #%d: %s" % (i+1, "NO")
    else:
        print "Case #%d: %s" % (i+1, "YES")
