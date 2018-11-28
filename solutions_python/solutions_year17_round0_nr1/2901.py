filename  = "A-large.in" #"A-small-attempt0.in"
f = open(filename,'r')
out = open("output.out",'w')
T =int(f.readline())
for Ca in range(T):
    [S,K]=[j for j in f.readline().split()]
    K=int(K)
    #print(S+ " "+str(K))
    D = [0 if S[i] =="+"else 1 for i in range(len(S))]
    #print(str(D)+" D")
    Del = [D[0]]+[D[i]^D[i-1] for i  in range(1,len(D))]
    #print(str(Del)+" DEl")
    I=[j for j in Del]
    for i in range(K,len(I)):
        I[i] ^=I[i-K]
    #print(str(I)+" I")
    ret= str(sum(I))if sum(I[len(I)-K+1:])==0 else "IMPOSSIBLE"
    print("Case #"+str(Ca+1)+": "+ret)
    out.write("Case #"+str(Ca+1)+": "+ret+"\n")
f.close()
out.close()
