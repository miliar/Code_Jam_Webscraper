
f=open("tidyin.txt")
T=int(f.readline().strip())

def istidy(a):
    a=str(a)
    if a=="".join(sorted(list([i for i in a]))):
        return True
    return False
def findtidy(a):
    a=str(a)
    b=[]
    if istidy(a):
        return int(a)
    else:
        b.append(a[0])
        nines=False
        i=1
        while i < len(a):
            if a[i] <  a[i-1]:
                b[i-1]=str((int(b[i-1])-1) % 10)
                nines=True
                break
            else:
                b.append(a[i])
            i+=1
        if nines:
            for k in range(i,len(a)):
                b.append("9")
        
        if istidy(int("".join(b))):
            return int("".join(b))
        else:
            return findtidy(int("".join(b)))
answerlist=[]
for line in f:
    a=int(line.strip())
    answerlist.append(findtidy(a))
g=open("tidyout.txt","w")
for i in range(0,len(answerlist)):
    g.write("Case #"+str(i+1)+": "+str(answerlist[i])+"\n")
f.close()
g.close()
    
