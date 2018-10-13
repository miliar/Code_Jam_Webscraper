#!/usr/bin/python

fi = open("a.in","r")
fo = open("a.out","w")
t = fi.readline()
testNo = 0
for line in fi:
    instr,k = line.split(" ")
    instr = [1 if x== '+' else -1 for x in instr]
    k = int(k)
    ans = 0
    for i in range(len(instr)-k+1):
        if instr[i] == -1:
            instr[i:(i+k)] = [x*-1 for x in instr[i:(i+k)]]
            ans += 1
    for i in instr[len(instr)-k:]:
        if i == -1:
            ans = 'IMPOSSIBLE'
            break
    testNo += 1
    if ans == 'IMPOSSIBLE':
        outstr = "Case #%d: IMPOSSIBLE\n"%(testNo)
    else:
        outstr = "Case #%d: %d\n"%(testNo,ans)
    fo.write(outstr)
