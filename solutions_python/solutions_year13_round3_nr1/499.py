f=open("A-small-attempt0.in","r")
f2=open("ans.out","w")
cases=int(f.readline())
for i in range(cases):
    tem=f.readline().split()
    #tem=raw_input().split()
    word,n=tem[0],int(tem[1])
    ls=[]
    count=0
    for j in range(len(word)-n+1):
        bo=True
        for k in range(j,j+n):
            if  word[k] in ['a','e','i','o','u']:
                bo=False
                break
        if bo==True:
            ls.append(word[j:j+n])
    subls=[]
    for sub in ls:
        for j in range(len(word)-n+1):
            for k in range(j,len(word)+1):
                x=word[j:k]
                if sub in x and (j,k) not in subls:
                    subls.append((j,k))
                    count+=1
    #print subls
    f2.write("Case #%d: %d\n"%(i+1,count))
f.close()
f2.close()