import sys

def minute(s):
    s=s.split(":")
    return int(s[0])*60+int(s[1])

def case(i, f):
    line=f.readline().strip()
    T=int(line)
    line=f.readline().strip()
    NA,NB=[int(x) for x in line.split(" ")]
    A2B_a=[]
    A2B_b=[]
    B2A_a=[]
    B2A_b=[]
    for j in range(NA):
        line=f.readline().strip()
        t=line.split(" ")
        A2B_a.append(minute(t[0]))
        A2B_b.append(minute(t[1])+T)
    for j in range(NB):
        line=f.readline().strip()
        t=line.split(" ")
        B2A_a.append(minute(t[0]))
        B2A_b.append(minute(t[1])+T)

    a2b=calc(A2B_a, B2A_b)
    b2a=calc(B2A_a, A2B_b)

    print "Case #%d: %d %d" % (i+1, a2b, b2a)

def calc(outcome, income):
    outcome.sort()
    income.sort()
    
    c=0
    for i in outcome:
        try:
            v=income[0]
        except: v=None
        if v!=None:
            if i>=v: 
                income.pop(0)
                continue
        c+=1
    return c


def go(name):
    f=file(name)

    line=f.readline().strip()
    total=int(line)
    for i in range(total):
        case(i, f)
    
    f.close()
try:
    fn=sys.argv[1]
except:
    print "Usage:\n", "python", sys.argv[0]+" input_file_name"
    sys.exit(1)

go(fn)
