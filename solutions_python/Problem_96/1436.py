a = []
out = open("out.txt", "w")
casenum = 1
for line in open("in.txt", "rU").readlines()[1:]:
    ans = 0
    line = map(int, line[:-1].split(" "))
    n, s, p, t = line[0], line[1], line[2], line[3:]
    for guy in t:
        hi = guy / 3
        if guy % 3:
            hi += 1
        if hi >= p:
            ans += 1
        elif guy % 3 != 1 and s > 0 and hi + 1 >= p and guy != 0:
            ans += 1
            s -= 1

    print "Case #" + str(casenum) + ": " + str(ans)
    out.write("Case #" + str(casenum) + ": " + str(ans) + "\n")
    casenum += 1

out.close()
