fi = open('A-small-attempt0.in')
fo = open('A-small-attempt0.out', 'wb')

def read_int():
    return int(fi.readline().rstrip("\n"))

def read_int_array():
    a = []
    s = fi.readline().rstrip("\n").split(" ")
    for i in s:
        a.append(int(i))
    return a


T = read_int()
for j in xrange(T):
    L1 = read_int()
    for i in xrange(4):
        if (i == L1 - 1):
            S1 = read_int_array()
        else:
            read_int_array()
    L2 = read_int()
    for i in xrange(4):
        if (i == L2 - 1):
            S2 = read_int_array()
        else:
            read_int_array()

    c = set(S1).intersection(set(S2))

    if len(c) == 0:
        fo.write("Case #%d: Volunteer cheated!\n" % (j+1))
    elif len(c) == 1:
        fo.write("Case #%d: %d\n" % (j+1, c.pop()))
    else:
        fo.write("Case #%d: Bad magician!\n" % (j+1))


fi.close()
fo.close()