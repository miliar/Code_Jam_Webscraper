import os

fin = "A-large.in"
fout = "A-large.out"
fr = open(fin,"r")
fw = open(fout,"w")

T = int(fr.readline())
for i in range(T):
    S = list(fr.readline())   
    S.pop()
    sp = S.index(' ') + 1
    N = int(S[0])
    S = [int(j) for j in S[sp:]]
    
    count = 0
    frnd = 0
    for j in range(len(S)):
        if count < j:
            frnd = frnd + 1
            count = count + 1
        count = count + S[j]
    print(S, frnd)
    fw.write("Case #" + str(i + 1) + ": " + str(frnd))
    if i < T - 1:
        fw.write("\n")

fr.close()
fw.close()

