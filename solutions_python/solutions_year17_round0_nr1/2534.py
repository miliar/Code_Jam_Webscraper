if __name__ == "__main__":
    with open("a.in", "r") as r, open("a.out", "w") as w:
        t = int(r.readline().strip())
        for _ in range(t):
            s, k = r.readline().split()
            n, k = len(s), int(k)
            s = list(s)
            ans = 0
            for i in range(n - k + 1):
                if s[i] == "-":
                    ans += 1
                    for j in range(k):
                        s[i + j] = "-" if s[i + j] == "+" else "+"
            if "-" in s:
                w.write("Case #%d: IMPOSSIBLE\n" % (_ + 1))
            else:
                w.write("Case #%d: %d\n" % ((_ + 1), ans))
