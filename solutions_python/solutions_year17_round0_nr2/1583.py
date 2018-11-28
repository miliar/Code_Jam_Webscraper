f1=open("B-large.in","r")
data=f1.readlines()
k=int(data[0])
f2=open("results.txt","w")
for i in range(k):
    num=int(data[i+1])
    strnum=str(num)
    tidy=strnum
    l=len(strnum)
    mx=int(strnum[0])
    for j in range(1,l):
        x=int(strnum[j])
        if x<mx:
            half1 = str(int(strnum[:j])-1)
            half2 = str('9'*(l-j))
            if half1=='0':
                tidy=half2;
            elif int(half1)<=9 or int(half1[j-1])>=int(half1[j-2]):
                tidy=half1+half2
            elif half1[j-1]=='0':
                tidy='9'*(j-1)+half2
            else:
                hf1=['']*j
                k=j-2
                while (k>=0) and (int(half1[k])==int(half1[j-2])):
                    k-=1
                k+=1
                hf1=half1[:k]+half1[j-1]+'9'*(j-k-1)
                tidy=hf1+half2
            break
        else:
            mx=x
    f2.write("Case #"+str(i+1)+": "+tidy+"\n")

f1.close()
f2.close()
