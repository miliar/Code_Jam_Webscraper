from collections import deque

with open("in.txt", "r") as f:
    sets = []
    w = f.read().split("\n")
    for x in range(1, int(w[0]) + 1):
        s, k = w[x].split(" ")
        sets.append({"s": [True if y is "+" else False for y in s], "k": int(k)})

    def flip(i, s, k, n):
        # sb = s[:]

        for x in range(i, i + k):
            s[x] = not s[x]

        # print(n, i, i + k, len(s), sb, s)
        return s

    def ite(root, k):
        a = []
        q = deque()

        a.append(root)
        q.append((0, root))

        m = len(root) - k + 1

        while len(q) > 0:
            n, cur = q.popleft()

            if all(y for y in cur):
                return (n, cur)

            if n >= 100:
                continue

            for i in range(0, m):
                sn = flip(i, cur[:], k, n)

                if sn not in a:
                    a.append(sn)
                    q.append((n + 1, sn))

        return (-1, s)

    i = 0
    for s in sets:
        i += 1
        n, r = ite(s["s"], s["k"])

        if n < 0:
            n = "IMPOSSIBLE"

        print("Case #" + str(i) + ": " + str(n))
