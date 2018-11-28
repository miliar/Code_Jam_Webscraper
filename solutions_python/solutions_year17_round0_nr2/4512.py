def ND(n):
    out = True
    while(n!=0):
        x_2 = n%10
        x_1 = int((n%100)/10)
        #print(x_1,x_2)
        if x_2<x_1:
            out = False
            break
        n = int(n/10)
    nDigits = 0
    for i in range(30):
        if int(n/(10**i))==0:
            nDigits = i
            break
    return (out,nDigits)

fname = "B-small-attempt0.in"
with open(fname) as f:
    content = f.readlines()
content = [x.strip() for x in content] 
f = open('Output.txt','w')
T = int(content[0])

for i in range(1,T+1):
    N = int(content[i])
    (isND,nDigits) = ND(N)
    
    N_temp = N
    while(not isND):
        x_1 = int(N_temp/(10**(nDigits-1)))
        x_2 = int(N_temp/(10**(nDigits-2)))%10
        if x_1>x_2:
            temp = (N%(10**(nDigits-1))+1)
            N = N-temp
            N_temp = N
            (isND,nDigits) = ND(N)
        else:
            N_temp = N_temp%(10**(nDigits-1))
            nDigits = nDigits-1
    print("Case #{}:".format(i),N, file=f)
    
f.close()