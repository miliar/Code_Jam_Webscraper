t=int(raw_input())
for j in range(1,t+1):
    n=int(raw_input())
    x=raw_input()
    x=x.split()
    minimumelt=10000000
    patricksum=0
    seansum=0
    for i in range(n):
        patricksum=patricksum^int(x[i])
        seansum=seansum+int(x[i])
        if int(x[i])<minimumelt:
            minimumelt=int(x[i])
    seansum=seansum-minimumelt
    s="Case #"
    s=s+str(j)
    s=s+": "
    if patricksum==0:
        s=s+str(seansum)
    else:
        s=s+"NO"
    print s
