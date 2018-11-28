filename  = "A-large.in" #
f = open(filename,'r')
out = open("output.out",'w')
T =int(f.readline())
for Ca in range(T):
    [D,N]=[int(j) for j in f.readline().split()]
    V= [[int(j) for j in f.readline().split()] for i in range(N)]
    arr = D/max([(D-V[i][0])/V[i][1] for i in range(N)])
    ret= str(arr)
    print("Case #"+str(Ca+1)+": "+ret)
    out.write("Case #"+str(Ca+1)+": "+ret+"\n")
f.close()
out.close()
