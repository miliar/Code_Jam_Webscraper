import sys

def lineitems():
    return sys.stdin.readline().strip().split(' ')

def urects(lrec, rrec):
    if lrec is None:
        return rrec
    if rrec is None:
        return lrec
    [u1,d1,l1,r1] = lrec
    [u2,d2,l2,r2] = rrec
    return (min(u1, u2), max(d1, d2), min(l1, l2), max(r1, r2))

def single(r, c):
    return [r,r,c,c]

def contains(rect, p):
    [u, d, l, r] = rect
    (row, col) = p
    return row >= u and row <= d and col >= l and col <= r

def main():
    numCases = int(sys.stdin.readline().strip())
    for caseNum in range(1, numCases + 1):
        print("Case #%d:" % caseNum)
        [rows, cols] = map(int, lineitems())
        pos = {}
        for r in range(rows):
            l = sys.stdin.readline().strip()
            for c in range(cols):
                v = l[c]
                if v != '?':
                    pos[v] = urects(pos.get(v, None), single(r, c))
        ks = list(pos.keys())
        def iscontained(*p):
            res = any(contains(v,p) for v in pos.values())
            return res
        for k in ks:
            v = pos[k]
            while True:
                [u,d,l,r] = v
                if l == 0:
                    break
                for y in range(u,d+1):
                    if iscontained(y,l-1):
                        break
                else:
                    v[2] -= 1
                    continue
                break
            while True:
                [u,d,l,r] = v
                if r == cols - 1:
                    break
                for y in range(u,d+1):
                    if iscontained(y,r+1):
                        break
                else:
                    v[3] += 1
                    continue
                break
            while True:
                [u,d,l,r] = v
                if u == 0:
                    break
                for x in range(l,r+1):
                    if iscontained(u-1,x):
                        break
                else:
                    v[0] -= 1
                    continue
                break
            while True:
                [u,d,l,r] = v
                if d == rows - 1:
                    break
                for x in range(l,r+1):
                    if iscontained(d+1,x):
                        break
                else:
                    v[1] += 1
                    continue
                break
        for r in range(rows):
            for c in range(cols):
                for (k,v) in pos.items():
                    if contains(v,(r,c)):
                        print(k,end='')
                        break
            print()

if __name__ == '__main__':
    main()
