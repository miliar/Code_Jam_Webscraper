def War(LN,LK):
    kem=0
    nao=0
    temp1=[]+LN
    temp2=[]+LK
    f = 0
    for i in LN:
        for j in LK:
            if j > i:
                if (i in temp1)and (j in temp2):
                    temp1.pop(temp1.index(i))
                    temp2.pop(temp2.index(j))
                    kem+=1
                    f = 1
                    break
        if not f:
            temp1.pop(temp1.index(i))
            temp2.pop(0)
            
            
    return kem

def DWar(LN,LK):
    kem=0
    nao=0
    temp1=[]+LN
    temp2=[]+LK
    for i in LN:
        if i < min(temp2):
            temp1.pop(temp1.index(i))
            temp2.pop(-1)
            kem+=1
        else:
            temp1.pop(temp1.index(i))
            temp2.pop(0)
            nao+=1
            
    return nao

File=open("D-small-attempt2.in","r")
Output=open("try.out","w")
data=File.read().splitlines()
#print data
n=data[0]
Naomi=[]
Kem=[]
N=[]
result=""
for i in range (1,(int(n)*3)-1,3):
    N.append(i)
for i in range (2,(int(n)*3),3):
    Naomi.append(i)
for i in range (3,(int(n)*3)+1,3):
    Kem.append(i)
#print sorted(data[Naomi[i]].split(" "))
#print sorted(data[Kem[i]].split(" "))
#print N
#print n,len(Naomi), len(Kem), len(N)
for i in range(0,int(n)):
    #print sorted(data[Naomi[i]].split(" "))
    #print sorted(data[Kem[i]].split(" "))
    #print DWar(sorted(data[Naomi[i]].split(" ")),sorted(data[Kem[i]].split(" ")))
    #print int(data[N[i]])
    #print sorted(data[Naomi[i]].split(" "))
    #print sorted(data[Kem[i]])
    #print War(sorted(data[Naomi[i]].split(" ")),sorted(data[Kem[i]].split" ")))
    War1=int(data[N[i]])-War(sorted(data[Naomi[i]].split(" ")),sorted(data[Kem[i]].split(" ")))
    DWar1=DWar(sorted(data[Naomi[i]].split(" ")),sorted(data[Kem[i]].split(" ")))
    result=result+"Case #"+str(i+1)+": "+str(DWar1)+" "+str(War1)+" \n"

#print result
Output.write(result)
Output.close()



        
    
