import sys
fin = open("A-small-attempt0.in","r")
inp = fin.readline
fout = open("magic_output","w")
out = fout.write
t = int(inp())
for case in xrange(1,t+1):
    m1 = []
    m2 = []
    r1 = int(inp())-1
    for i in range(4):
        m1.append(map(int,inp().split()))
    r2 = int(inp())-1
    for j in range(4):
        m2.append(map(int,inp().split()))
    cnt = 0
    for c1 in range(4):
        for c2 in range(4):
            if m1[r1][c1] == m2[r2][c2]:
                ans = m1[r1][c1]
                cnt+=1
    if cnt > 1:
        out("Case #"+str(case)+": Bad magician!\n")
    elif cnt == 1:
        out("Case #"+str(case)+": "+str(ans)+"\n")
    else:
        out("Case #"+str(case)+": Volunteer cheated!\n")
    t-=1
fin.close()
fout.close()
