

filename = open("C-small-attempt1.in",'r')
s1 = filename.readlines()
for i in range(len(s1)):
    s1[i] = s1[i].replace("\n","")
cases  = int(s1[0])



filename.close()
newFile = open("output.in","w")

for i in range(cases):
    newFile.writelines("Case #%s:"%(i+1))
    newFile.writelines("\n")
    numbers=s1[i+1][3:].split()
    n=[]
    for i in numbers:
        n.append(int(i))
        

    from itertools import combinations
    s=[]

    for i in range(1,21):
        x=combinations(n,i)
        for i in x:
            s.append([sum(i),i])

            
    clist=[]
    for i in range(1,2000001):
        clist.append([i,[]])

    for i in s:
        clist[i[0]][1].append(i)

    def checker(x):
        a=[]
        for i in x[1]:
            for j in i[1]:
                a.append(j)
        return len(a)==len(set(a))
        
    z=[]
    for i in clist:
        if len(i[1])>1:
            if checker(i):
                #print i
                z.append(i)
                break
            else:
                continue

    if len(z)==0:
        newFile.writelines("Impossible")
        newFile.writelines("\n")
    else:
        for i in z:
            j=i[1]
            for q in j:
                for w,t in enumerate(q[1]):
                    if w==len(q[1])-1:
                        newFile.writelines(str(t))
                    else:
                        newFile.writelines(str(t))
                        newFile.writelines(" ")
                newFile.writelines("\n")
                
        
newFile.close()
