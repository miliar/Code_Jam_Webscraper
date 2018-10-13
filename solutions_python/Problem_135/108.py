from datetime import datetime

#Input
fName = raw_input('Enter Filename of Input:\n')
with open(fName) as f:
    inp = [line.rstrip() for line in f]
#Output
timestamp = datetime.now().strftime("%H.%M.%S")
out = open(timestamp+'.out', 'w')
#Stuff
caseCount = int(inp[0])
for case in range(1,caseCount+1):
    off = 1+10*(case-1)
    off2 = off+5
    row = int(inp[off])
    row2 = int (inp[off2])
    in1 = inp[off+row].split()
    in2 = inp[off2+row2].split()
    poss = set(in1)&set(in2)
    pri = 'Case #'+str(case)+': '
    cho = len(poss)
    if cho == 0:
        pri += 'Volunteer cheated!'
    elif cho ==1:
        pri += poss.pop()
    else:
        pri += 'Bad magician!'
    out.write(pri+'\n')
out.close()
