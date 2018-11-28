from collections import deque
x=int(raw_input())
for i in range(x):
    q1=deque([])
    q2=deque([])
    y=raw_input()
    y=y.split()
    ind=0
    n=int(y[ind])
    ind=ind+1
    r=[]
    p=[]
    for j in range(n):
        r.append(y[ind])
        #r[j]=y[ind]
        ind=ind+1
        #p[j]=y[ind]
        p.append(int(y[ind]))
        ind=ind+1
        if r[j]=='O':
            q1.append(p[j])
        if r[j]=='B':
            q2.append(p[j])
    pos1=1
    pos2=1
    total=0
    #print total
    #print len(q1), len(q2)
    for j in range(n):
        if r[j]=='O':
            numSteps=abs(q1[0]-pos1)+1
            pos1=q1[0]
            if len(q2)>0 and pos2<q2[0]:
                pos2=min(pos2+numSteps,q2[0])
            elif len(q2)>0 and pos2>q2[0]:
                pos2=max(pos2-numSteps,q2[0])
            q1.popleft()
            total=total+numSteps
        elif r[j]=='B':
            numSteps=abs(q2[0]-pos2)+1
            pos2=q2[0]
            if len(q1)>0 and pos1<q1[0]:
                pos1=min(pos1+numSteps,q1[0])
            elif len(q1)>0 and pos1>q1[0]:
                pos1=max(pos1-numSteps,q1[0])
            q2.popleft()
            total=total+numSteps
        #print total
    s="Case #"
    s=s+str(i+1)
    s=s+": "
    s=s+str(total)
    print s
    #print "Case #%(testcase): %(total)".format(i+1,total)
