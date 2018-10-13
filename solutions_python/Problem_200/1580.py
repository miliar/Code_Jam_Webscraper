fi = open("B-large.in", "r")
fo = open("B.out", "w")
T = int(fi.readline().rstrip())
for t in range(1, T + 1):
    s = fi.readline().rstrip()
    n = len(s)
    can = 0
    for i in range(n):
        if i != 0 and int(s[i]) > 0 and int(s[i]) - 1 >= int(s[i - 1]):
            can = i
        if i < n - 1 and s[i] > s[i + 1]:
            ii = can
            ans = s[:ii] + str(int(s[ii]) - 1) + "9" * (n - ii - 1)
            s = ans
            break
    fo.write(("Case #%d: " % t) + str(int(s)) + "\n")