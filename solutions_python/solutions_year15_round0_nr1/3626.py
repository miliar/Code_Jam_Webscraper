file= open('A-small-attempt1.in','r')
outfile=open('Small-Aout','w')
T = int(file.readline())
outs=[]
for i in range(T):
    S=file.readline()
    Smax=int(S[0])
    S=S[2:].rstrip()
    S=[int(x) for x in S]
    counter=0
    if S[0]==0:
        S[0]+=1
        counter+=1
    for index in range(len(S[1:])):
        shyness=index+1
        if S[shyness] > 0:
            if sum(S[:shyness])<shyness:
                ss=(shyness-(sum(S[:shyness])))
                print(sum(S[:shyness]),shyness,S[0],counter)
                counter+=ss
                S[0]+=ss
                print(sum(S[:shyness]),shyness,S[0],counter)
    outfile.write("Case #{0}: {1}\n".format(i+1,counter))
file.close()
outfile.close()
        
        
    
    
    
            

            
            
        
