inp = open("in.txt", "r")
out = open("out.txt","w")
T= int((inp.readline()).rstrip())
for i in range(T):
    Ns=list(map(int,list((inp.readline()).rstrip())))
    if len(Ns)==1:
        out.write("Case #" + str(i+1) + ": " + str(Ns[0]) + "\n")
    else:
        while not(all(Ns[k] <= Ns[k+1] for k in range(len(Ns)-1))):
            flag = 0
            for j in range(len(Ns)-1):
                if flag==0:
                    if Ns[j]>Ns[j+1]:
                        Ns[j]-=1
                        flag=1
                else:
                    Ns[j]=9
                if flag == 1 and j==len(Ns)-2:
                    Ns[j+1]=9
        NNs=list(map(str,Ns))
        N=int(''.join(NNs))
        out.write("Case #" + str(i+1) + ": " + str(N) + "\n")
