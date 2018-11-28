import string

ifile = open("C-small-attempt0.in")
fs = ifile.read().split("\n")
ifile.close()

T = int(fs[0])

out = []

NMidx = 1
for t in range(0,T):
    line = fs[NMidx].split(' ')
    N = int(line[0])
    L = int(line[1])
    H = int(line[2])
    line = fs[NMidx+1].split(' ')
    notes = [int(i) for i in line]

    impos = True
    for i in range(L,H+1):
        fail = False
        for n in notes:
            if i % n==0 or n%i==0:
                pass
            else:
                fail=True
                break
        if not fail:
            impos = False
            sol = i
            break
    if impos:
        out.append("Case #"+str(t+1)+": %s"%'NO')
    else:
        out.append("Case #"+str(t+1)+": %s"%str(sol))
    NMidx+=2

ofile = open("output.txt","w")
ofile.write(string.join(out,"\n"))
ofile.close()
