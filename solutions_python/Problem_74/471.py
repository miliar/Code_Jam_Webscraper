import sys

def solve(seq):
    t = 0
    o_val = 0
    last_b_v = 1
    last_o_v = 1
    b_val = 0
    for p in seq:
        c = p[0]
        v = int(p[1:])
        if c == 'O':
            v1 = o_val + abs(v - last_o_v) + 1
            last_o_v = v
            v = v1
        else:
            v1 = b_val + abs(v - last_b_v) + 1
            last_b_v = v
            v = v1
        if v > t:
            t = v
        else:
            t = t + 1
        if c == 'O':
            o_val = t
        else:
            b_val = t
    return t
        
        

def do_bottrust(s,ctr):
    seq = []
    parts = s.split()
    c = ''
    for p in parts[1:]:
        if p == 'O' or p == 'B':
            c = p
        else:
            seq.append(c+p)
    v = solve(seq)
    print "Case #%s: %s" % (ctr,v)


if __name__ == "__main__":
    f = open(sys.argv[1])
    n = int(f.readline())
    for i in range(0,n):
        s = f.readline().strip()
        if s[0] == '#':
            continue
        do_bottrust(s,i+1)
    f.close()
