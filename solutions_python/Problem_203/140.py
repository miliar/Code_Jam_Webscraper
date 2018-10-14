import re

if __name__ == "__main__":
    with open("a.in", "r") as r, open("a.out", "w") as w:
        t = int(r.readline().strip())
        for _ in range(t):
            n, m = map(int, r.readline().strip().split())
            a = []
            for i in range(n):
                a.append(list(r.readline().strip()))
            for i in range(n):
                for j in range(m):
                    if a[i][j] != "?":
                        for k in range(j - 1, -1, -1):
                            if a[i][k] == "?":
                                a[i][k] = a[i][j]
                            else:
                                break
                for j in range(m - 1, -1, -1):
                    if a[i][j] != "?":
                        break
                for k in range(j + 1, m):
                    a[i][k] = a[i][j]
            for i in range(n):
                if len(re.findall(r"\?{%d}" % m, "".join(a[i]))) == 0:
                    for j in range(i - 1, -1, -1):
                        if len(re.findall(r"\?{%d}" % m, "".join(a[j]))) != 0:
                            a[j] = a[i]
                        else:
                            break
            for i in range(n - 1, -1, -1):
                if len(re.findall(r"\?{%d}" % m, "".join(a[i]))) == 0:
                    break
            for j in range(i + 1, n):
                a[j] = a[i]
            w.write("Case #%d:\n" % (_ + 1))
            for i in range(n):
                w.write("".join(a[i]) + "\n")
