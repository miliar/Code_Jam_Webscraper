inputF=open("input.txt","r")
outputF=open("output.txt","w")

T=int(inputF.readline().strip())

for i in range(1,T+1):
    A,B,K=inputF.readline().split(" ")
    a=list(range(int(A)))
    b=list(range(int(B)))
    k=list(range(int(K)))
    win=0
    for item in a:
        for item2 in b:
            if item&item2 in k:
                win+=1
    outputF.write("Case #"+str(i)+": "+str(win)+"\n")
