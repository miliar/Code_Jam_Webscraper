
if __name__ == "__main__":
    fin = open("B-large.in", "r")
    fout = open("B-large.out", "w")
    T = int(fin.readline())
    for cas in range(T):
        l = fin.readline().strip().split()
        n, s, p = map(int, l[:3])
        total = map(int, l[3:])
        if p == 0:
            ans = n
        elif p == 1:
            ans = sum(v > 0 for v in total)
        else:
            need = sum(3 * p - 4 <= v and v <= 3 * p - 3 for v in total)
            above = sum(v >= 3 * p - 2 for v in total)
            ans = above + min(need, s)
        print  >> fout, ("Case #%d: %s" % (cas + 1, ans))
