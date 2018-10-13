#fd = open("debug.txt", "w")
result_string = ['NO', 'YES']

def print_result(f, c, r):
    f.write("Case #%d: %s\n" % (c, result_string[r]))

#(h, r, c)
def t_cmp(t1, t2):
    return cmp(t1[0], t2[0])


def make_lawn(f, n):
    l = []
    for i in xrange(1, n+1):
        d = f.readline()
        #print >> fd, d.strip()
        ll = map(int, d.strip().split())
        l.extend([(ll[j], i, j+1) for j in xrange(len(ll))])
    return l

def check_possibility(l, t, N, M):
    h, n, m = t
    r = [l[(n-1)*M + i][0] for i in range(1, M+1)]
    c = [l[m + i][0] for i in range(0, N*M, M)]
    rr = not any(filter(lambda v: v > h, r))
    cr = not any(filter(lambda v: v > h, c))
    #print >> fd, "r = ", r, rr
    #print >> fd, "c = ", c, cr
    #print >> fd, n, m, h
    return cr or rr


def main():
    f = open("B-large.in")
    fo = open("B-large.out", 'w')
    size = int(f.readline())
    #print >> fd, size
    for i in xrange(1, size+1):
        N, M = map(int, f.readline().strip().split())
        #print >> fd, "\n"
        l = make_lawn(f, N)
        sl = sorted(l[:], cmp=t_cmp)
        l.insert(0, 0)
        found = 1
        for s in sl:
            if not check_possibility(l, s, N, M):
                found = 0
                break
        print_result(fo, i, found)
    f.close()
    fo.close()

main()
