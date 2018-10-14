filename  = "B-large.in"#"B-sample.in"
f = open(filename,'r')
out = open("output.out",'w')
T =int(f.readline())
for Ca in range(T):
    S= f.readline().split()[0]
    i=0
    while(i<len(S)-1) and S[i]<=S[i+1]:
        i+=1
    S2 =S
    #print("i "+str(i)+ " lens " +str(len(S))+ "a"+S+"a")
    if i < len(S)-1:
        while (i>0) and (S[i-1]==S[i]):
            i-=1
        S2=S[:i]+str(int(S[i])-1)+("9"*(len(S)-i-1))
        #TODO trim zeros
        i=0
        while (i<len(S2))and(S2[i]=="0"):
            i+=1
        S2 =S2[i:]
    #print(i)
    ret=S2
    print("Case #"+str(Ca+1)+": "+ret)
    out.write("Case #"+str(Ca+1)+": "+ret+"\n")
f.close()
out.close()
