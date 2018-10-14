import sys

def steps_impl(A, data, s, sup):
    while data and A > data[0]:
        A += data.pop(0)
    left = len(data)
    if left == 0:
        return s
    s += 1
    if left == 1 or s == sup:
        return s
    A = 2 * A - 1
    return steps_impl(A, data, s, min(s + left - 1, sup))

def steps(A, data):
    data.sort()
    return steps_impl(A, data, 0, len(data))

f = open(sys.argv[1])
T = int(f.readline())
for t in xrange(1,T+1):
    a = int(f.readline().strip()) - 1
    row_a = None
    for i in range(4):
        l = f.readline()
        if i == a:
            row_a = l.strip().split()

    b = int(f.readline().strip()) - 1
    row_b = None
    for i in range(4):
        l = f.readline()
        if i == b:
            row_b = l.strip().split()

    cnt, res = 0, "Volunteer cheated!"
    for x in row_a:
        if x in row_b:
            cnt += 1
            res = x
    if cnt > 1:
        res = "Bad magician!"
    print "Case #{0}: {1}".format(t, res)
