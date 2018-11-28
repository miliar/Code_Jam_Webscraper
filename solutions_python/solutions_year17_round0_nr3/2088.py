andmed=open("t.in","r")
t=int(andmed.readline())
vastused=list()
for i in range(t):
    tempr=andmed.readline().split()
    n=int(tempr[0])
    k=int(tempr[1])
    lenl=list()
    lenl.append(n)
    for j in range(k):
        lambdas=max(lenl)
        miin=(lambdas-1)//2
        maks=lambdas//2
        lenl.append(miin)
        lenl.append(maks)
        lenl.remove(max(lenl))
    vastus="Case #"+str(i+1)+": "+str(maks)+" "+str(miin)
    vastused.append(vastus)
andmed.close()

outgo=open("t.out","w")
for asi in vastused:
    outgo.write(asi)
    outgo.write("\n")
outgo.close()
