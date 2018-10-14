import math
with open("C-small-2-attempt0.in") as file:
    arr=file.readlines()
cases=int(arr[0])
for case in range(cases):
    larr=arr[case+1].split()
    N=int(larr[0])
    K=int(larr[1])
    x=math.floor(math.log(K,2))
    numel=math.pow(2,x)
    sumel=N+1-numel
    zbase=math.floor(float(sumel)/numel)
    diff=sumel-zbase*numel
    if(K-numel<diff):
        z=zbase+1
    else:
        z=zbase
    r=math.ceil(float(z-1)/2)
    l=z-r-1
    print("Case #{}: {} {}".format(case+1,r,l))
