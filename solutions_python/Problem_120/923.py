def suma(x):
    return (((2*r+1)+(2*r+1+4*x-4))*x*1)/2
T=int(input());
for x in range(T):
    r,t=map(int, input().split());
    lewo,prawo,sr=0,1000000000000000000,0;
    while lewo<prawo:
        sr=int((lewo+prawo+1)/2);
        #print(suma(sr),"\n")
        if suma(sr)<=t:
            lewo=sr
        else:
            prawo=sr-1
    print("Case #{0}: {1}\n".format(x+1,lewo))
