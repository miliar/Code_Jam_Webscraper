import math

with open('c.out', 'w') as f:
    m = int(input())
    for c in range(m):
        n, k = map(int, input().split())
        q = {n: 1}
        w = {n}
        l = r = 0
        while k > 0:
            s = max(w)
            w.remove(s)

            g = q[s]
            s -= 1
            l = math.ceil(s / 2)
            r = math.floor(s / 2)
            k -= g
            if l > 0:
                q[l] = g + q.get(l, 0)
                w.add(l)
                if r > 0:
                    q[r] = g + q.get(r, 0)
                    w.add(r)
            print(len(w))

        # for _ in range(k):
        #     s = q.pop() - 1
        #     l = math.ceil(s / 2)
        #     r = math.floor(s / 2)
        #     if l > 0: insort(q, l)
        #     if r > 0: insort(q, r)
        print('Case #{0}:'.format(c + 1), l, r, file=f)
