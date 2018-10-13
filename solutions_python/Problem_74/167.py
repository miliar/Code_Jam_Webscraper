input=open("int","r")
out=open("out","w")
n=int(input.readline())

for s in xrange(n):
    case=input.readline().split(" ")
    case=case[1:]
    O=[]
    B=[]
    Q=[]
    for i in range(len(case)):
        if case[i]=="O":
            O.append(int(case[i+1]))
            Q.append("O")
        elif case[i]=="B":
            B.append(int(case[i+1]))
            Q.append("B")

    O.reverse()
    B.reverse()
    Q.reverse()

    d1=0
    d2=0
    timer=0

    pos1=1
    pos2=1
    while 1:
        if not Q:break

        if O:
            if(pos1<O[-1]):d1=1
            elif(pos1>O[-1]):d1=-1
            elif(pos1==O[-1]):d1=0
        if B:
            if(pos2<B[-1]):d2=1
            elif(pos2>B[-1]):d2=-1
            elif(pos2==B[-1]):d2=0
        

        if O and Q[-1]=="O":
            if(pos1!=O[-1]):pos1+=d1
            elif pos1==O[-1]:
                O.pop()
                Q.pop()
            pos2+=d2
        elif len(B):
            if(pos2!=B[-1]):pos2+=d2
            elif pos2==B[-1]:
                B.pop()
                Q.pop()
            pos1+=d1
        timer+=1

    out.write('Case #%s: %s\n' %((s+1).__str__(),timer.__str__()))