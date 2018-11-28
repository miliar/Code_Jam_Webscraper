from math import log
tc=int(input("TC"))
ans=[]
for t in range(tc):
    f=input()
    f=[int(i) for i in f.split("/")]
    n=f[0]
    d=f[1]
    if round((log(d)/log(2)),0)==log(d)/log(2):
        for i in range(40):
            if n/d - 1/(2**(i+1))>=0:
                ans.append(i+1)
                break
        else:
            ans.append('impossible')
    else:
        ans.append('impossible')
for i in range(len(ans)):
    print("Case #"+str(i+1)+": "+str(ans[i]))

