testcases=input()
for t in range(testcases):
    N=int(raw_input())
    Nl=[i for i in str(N)]
    while sorted(Nl)!=Nl and N>0:
        N=N-1
        Nl=[int(i) for i in str(N)]
        #print(Nl)
        
    print("Case #"+str(t+1)+': '+str(N))
