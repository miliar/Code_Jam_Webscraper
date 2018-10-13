inf = open('A-large.in')
cases = inf.readline().strip()
out = open('out.dat','w')
for case in range(int(cases)):
    spline = inf.readline().strip().split(' ')
    maxv = int(spline[0])
    lvls = spline[1]

    people = 0
    addit = 0

    for lvl in range(maxv+1):
        lvlp = int(lvls[lvl])
        if lvl>people and lvlp>0:
            addit+=(lvl-people)
            people+=(lvl-people)
        people+=lvlp

    out.write("Case #"+str(case+1)+": "+str(addit)+"\n")

out.close()
