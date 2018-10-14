#!/usr/bin/python

fi = open("a.in","r")
fo = open("a.out","w")
t = fi.readline()
testNo = 0
for line in fi:
    inp = list(line)
    inp = map(int, [x for x in inp if x!='\n'])
    carry = 0
    outstr = ""
    testNo += 1
    if len(inp) == 1:
        outstr = "Case #%d: %d\n"%(testNo,inp[0])
    else:
        prev = 0
        ind = 0
        outstr = ''.join([str(x) for x in inp])
        for i in range(len(inp)-1):
            if inp[i] > inp[i+1]:
                inp[ind] -= 1
                inp[ind+1:] = [9 for _ in inp[ind+1:]]
            if inp[i] < inp[i+1]:
                ind = i+1
        if inp[0] == 0:
            inp = inp[1:]
        outstr = ''.join([str(x) for x in inp])
        if testNo == t:
            outstr = "Case #%d: %s"%(testNo,outstr)
        else:
            outstr = "Case #%d: %s\n"%(testNo,outstr)
    fo.write(outstr)
