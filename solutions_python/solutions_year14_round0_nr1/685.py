#f = open('Csample.in', 'r')
#f = open('C-small-practice.in', 'r')
f = open('A-small-attempt0.in', 'r')
outpu=open('output.txt','w')
cases = int(f.readline())
for case in range(cases):
    card1=int(f.readline())
    for i in range(4):
        if i == card1-1:
            A=[int(s) for s in f.readline().split(' ')]
        else:
            f.readline()
    card2=int(f.readline())
    for i in range(4):
        if i == card2-1:
            B=[int(s) for s in f.readline().split(' ')]
        else:
            f.readline()
    R=set(A).intersection(set(B))
    if len(R)==0:
        RS="Volunteer cheated!"
    elif len(R)>1:
        RS="Bad magician!"
    else:
        RS= str(next(iter(R)))
    outpu.write('Case #'+str(case+1)+": "+RS+'\n')
#"Bad magician!", "Volunteer cheated!", 
f.close()
outpu.close()
