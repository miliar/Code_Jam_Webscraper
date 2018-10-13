from modules.calc import calc

fi = open("input.txt", "r")
fo = open("output.txt", "w")

t = int(fi.readline().strip())

m1, m2 = calc()

for tests in range(t):
    s = list(fi.readline())
    for i in range(len(s)):
        if s[i] in m1:
            s[i] = m1[s[i]]
        else:
            s[i] = m2[s[i]]
    fo.write("Case #%d: " % (tests + 1) + "".join(s))