__author__ = 'PrimuS'

f = open("d:\\dev\\acm\\codeJam 2015\\A-large.in", "r")
of = open("d:\\dev\\acm\\codeJam 2015\\A_res_big.txt", "w")

T = int(f.readline())

for t in range(1, T + 1):
    s = f.readline().split()
    k = int(s[0])
    s = s[1].strip()
    res = 0
    cur = 0
    for i in range(len(s)):
        c = ord(s[i]) - ord('0')
        if c == 0:
            continue

        if cur < i:
            res += i - cur
            cur = i
        cur += c
    print("Case #{:d}: {:d}".format(t, res), file=of)

of.close()

