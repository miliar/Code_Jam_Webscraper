def fun(a,n,d):
    time=[]
    for i in range(n):
        tmp=1.0
        tmp=tmp*(d-a[i][0])/a[i][1]
        time.append(tmp)
    mx=max(time)
    return 1.0*d/mx

f_input=open("inputA.txt","r+")
f_output=open("outputA.txt","w+")
tc=int(f_input.readline())
for case in range(tc):
    d,n=map(int,f_input.readline().strip().split())
    a=[]
    for i in range(n):
        tmp=map(int,f_input.readline().strip().split())
        a.append(tmp)
    ans=fun(a,n,d)
    f_ans=str(ans)
    print f_ans
    f_output.write("Case #"+str(case+1)+": "+f_ans+"\n")
f_input.close()
f_output.close()
