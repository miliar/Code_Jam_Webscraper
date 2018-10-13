
def checkCase(caseData):
    caseTimes=[]
    O_pos=1
    B_pos=1
    O_good=0
    B_good=0
    min_time=0
    for case in caseData:
        pos=case[1]
        time=0
        if case[0]=="O":
            time=max(0,((O_pos - pos if O_pos > pos else pos - O_pos))-B_good)+1
            O_good+=time
            min_time+=time
            B_good=0
            O_pos=pos
        else:
            time=max(0,((B_pos - pos if B_pos > pos else pos - B_pos))-O_good)+1
            B_good+=time
            min_time+=time
            O_good=0
            B_pos=pos
        caseTimes.append((case[0],time))
    return min_time


data=open("A-large.in","r").read()

data=data.splitlines()[1:]
out=open("out.txt","w")
cases=[i.split(" ") for i in data]
for c in xrange(0, len(cases)):
    tmp=[]
    for i in xrange(1, len(cases[c]), 2):
        tmp.append((cases[c][i], int(cases[c][i+1])))
    out.write("Case #%i: %i\n"%(c+1,checkCase(tmp)))
    
out.close()
