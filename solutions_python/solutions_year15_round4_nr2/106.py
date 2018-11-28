def parse_float(s):
    r, d = s.split('.')
    return int(r) * 10000 + int(d)

for t in range(1, int(input()) + 1):
    print('Case #{}:'.format(t), end=' ')
    ns, vs, xs = input().split()
    n = int(ns)
    v = parse_float(vs)
    x = parse_float(xs)
    if n == 1:
        rs, cs = input().split()
        r, c = parse_float(rs), parse_float(cs)
        if x != c:
            print('IMPOSSIBLE')
        else:
            print('%.15f'%(v / r))            
    elif n == 2:
        rs1, cs1 = input().split()
        r1, c1 = parse_float(rs1), parse_float(cs1)
        rs2, cs2 = input().split()
        r2, c2 = parse_float(rs2), parse_float(cs2)
        if c1 == c2:
            c = c1
            r = r1 + r2
            if x != c:
                print('IMPOSSIBLE')
            else:
                print('%.15f'%(v / r))            
        elif x > max(c1, c2) or x < min(c1, c2):
            print('IMPOSSIBLE')
        else:
            p2 = (c1 - x) / (c1 - c2)
            p1 = 1 - p2
            t1 = p1 * v / r1
            t2 = p2 * v / r2
            print('%.15f'%max(t1, t2))
    else:
        for _ in range(n):
            rs1, cs1 = input().split()
    
    
    
