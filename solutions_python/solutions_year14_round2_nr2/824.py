tc=int(input("TC"))
ans=[]
for t in range(tc):
    a=input()
    a=[int(i) for i in a.split(" ")]
    k=a[2]
    count=0
    for i in range(a[0]):
        for j in range(a[1]):
            if(i & j < k):
                count+=1
    ans+=[count]
for i in range(len(ans)):
    print("Case #"+str(i+1)+": "+str(ans[i]))
