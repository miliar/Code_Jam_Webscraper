nums = set()
for k in range(101):
    nums.add(k)

sd = {}
s = set()
for i in range(11):
    for j in range(i):
        floatdiv = float(j)/float(i)
        if floatdiv*100.00 in nums:
            r = int(floatdiv*100)
            s.add(r)
            if r not in sd:
                sd[r] = i
s.add(100)
sd[100] = 1

f = open('A-small-attempt2.in', 'r')
cases = int(f.readline())
for case in range(cases):
    line = f.readline()
    l = [int(sp) for sp in line.split()]
    N = l[0]
    Pd = l[1]
    Pg = l[2]

    possible = "Broken"

    if Pg == 100:
        if Pd == 100:
            possible = "Possible"
    else:
        if Pd in s:
            if sd[Pd] <= N: #pg > 0
                if Pd == 0 and Pg == 0:
                    possible = "Possible"
                elif Pg == 0:
                    possible = "Broken"
                else:
                    possible = "Possible"

    print "Case #%s: %s" % (case+1, possible)


