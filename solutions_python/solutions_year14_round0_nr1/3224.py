in_file = open('A-small-attempt0.in','r')
out_file = open('Aout.txt','w')
n = int(in_file.readline())
for i in range(n):
    p =[]
    out =[]
    for t in range(2):
        r1=int(in_file.readline())
        for r in range(4):
            l=list(map(int,in_file.readline().split()))
            if ((r+1) == r1):
                p.append(l)
    for j in range(4):
        for k in range(4):
            if p[0][j] == p[1][k]:
                out.append(p[1][k])
    if len(out) == 1:
        out_file.write("Case #" + str(i+1) +": "+ str(out[0])+"\n")
    elif len(out) > 1:
        out_file.write("Case #" + str(i+1) +": "+ "Bad magician!\n")
    else:
        out_file.write("Case #" + str(i+1) +": "+ "Volunteer cheated!\n")
out_file.close()
in_file.close()
