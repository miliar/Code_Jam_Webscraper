T=input()
for i in range(T):
    l=2.00
    times=0
    c,f,x=[float(x) for x in raw_input().split()]
    while True:
        if(x/l<=c/l+(x/(l+f))):
            times+=x/l
            break
        else:
            times+=c/l
            l+=f
    print "Case #"+str((i+1))+": "+str(times)+"\n"
