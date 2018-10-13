fname = "A-small-attempt0"

fin = open(fname+".in")

T = map(int,fin.readline().strip().split())[0]

cases = []

for t in xrange(T):
    l1 = map(int,fin.readline().strip().split())[0]
    for x in xrange(1,5):
        if x==l1:
            s1 = set(map(int,fin.readline().strip().split()))
        else:
            fin.readline()
    l2 = map(int,fin.readline().strip().split())[0]
    for x in xrange(1,5):
        if x==l2:
            s2 = set(map(int,fin.readline().strip().split()))
        else:
            fin.readline()
    
    a = s1.intersection(s2)
    if len(a) ==0:
        cases.append(0)
    elif len(a) > 1 :
        cases.append(-1)
    elif len(a) == 1:
        cases.append(a.pop())
fin.close()

## Output
fout = open(fname+".out","w")

for t in xrange(1,T+1):
    line = "Case #"+str(t)+": "
    if cases[t-1] == -1:
        line += "Bad magician!\n"
    elif cases[t-1] == 0:
        line += "Volunteer cheated!\n"
    else:
        line+=str(cases[t-1])+"\n"
    fout.write(line)
fout.close()
            