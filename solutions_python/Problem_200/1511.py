#!/usr/bin/python

def main():
    with open ('B-large.in', 'r') as f, open('B-large.out', 'w') as g:
        t = int(f.readline().strip())
        for i in xrange(1, t+1):
            n = int(f.readline().strip())
            m = [int(x) for x in str(n)]
            o = []
            p = []
            for j in xrange(0, len(m)-1):
                o.append(m[j] > m[j+1])
                p.append(m[j] == m[j+1])
            q = next((j for j, k in enumerate(o) if k), -1)
            if q == -1:
                y = n
            else:
                r = q
                for j in xrange(q-1, -1, -1):
                    if not p[j]:
                        break
                    r=j
                z = []
                z.extend(m[0:r])
                z.append(m[r]-1)
                z.extend([9] * len(m[r+1:]))
                y = 0
                for j in xrange(0, len(z)):
                    y = y * 10
                    y = y + z[j]
            g.write("Case #{}: {}\n".format(i, y))


if __name__ == "__main__":
    main()