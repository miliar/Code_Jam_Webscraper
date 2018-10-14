from collections import deque

with open("C-small-attempt0.in") as fin:
    with open("C.out", "w") as fout:
        t = int(fin.readline())
        for j in range(1, t+1):
            (r, k, n) = tuple(int(x) for x in fin.readline().split(" "))
            g = deque([int(x) for x in fin.readline().split(" ")])
            cache = {}
            pos = 0
            y = 0
            total = sum(g)
            for i in range(r):
                filled = 0
                while g[0] + filled <= k and g[0] + filled <= total:
                    pos = (pos + 1) % n
                    size = g.popleft()
                    filled += size
                    g.append(size)
                y += filled
                cache[i] = y
                if pos == 0:
                    y = (r // (i + 1)) * y
                    if r % (i + 1) != 0:
                        y += cache[r % (i + 1) - 1]
                    break
            fout.write("Case #" + str(j) + ": " + str(y) + "\n")
            
