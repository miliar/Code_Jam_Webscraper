def cross(a, b, c):
    p1 = (b[0] - a[0], b[1] - a[1])
    p2 = (c[0] - b[0], c[1] - b[1])
    return p2[0] * p1[1] - p1[0] * p2[1]


def parts(_type=int):
    return map(_type, raw_input().split())

T = int(raw_input())

for z in range(T):
    N = int(raw_input())

    pts = []
    for i in range(N):
        a, b = parts(int)
        pts.append((a, b))

    print 'Case #{}:'.format(z + 1)
    if N == 1:
        print 0
    else:
        for i, a in enumerate(pts):
            q = N
            for j, b in enumerate(pts):
                if i == j:
                    continue
                cl, cr = 0, 0
                for k, c in enumerate(pts):
                    if i == j or j == k:
                        continue
                    t = cross(a, b, c)
                    # print a, b, t
                    if t < 0:
                        cl += 1
                    elif t > 0:
                        cr += 1
                q = min(q, cl, cr)
            print q
