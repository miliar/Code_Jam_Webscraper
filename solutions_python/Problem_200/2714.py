if __name__ == "__main__":
    with open("b.in", "r") as r, open("b.out", "w") as w:
        t = int(r.readline().strip())
        for _ in range(t):
            n = r.readline().strip()
            s = map(int, list(n))
            l = len(s)
            p = None
            for i in range(l - 1):
                if s[i] > s[i + 1]:
                    p = i
                    break
            if p == None:
                w.write("Case #%s: %s\n" % ((_ + 1), n))
                continue
            while p > 0 and s[p] == s[p - 1]:
                p -= 1
            s[p] -= 1
            for i in range(p + 1, l):
                s[i] = 9
            w.write("Case #%s: %s\n" % ((_ + 1), int("".join(map(str, s)))))
