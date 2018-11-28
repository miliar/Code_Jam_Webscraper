t=input()
for i in range(int(t)):
    freq=0
    flag=0
    pos=0
    n=list(input())
    for j in range(len(n)-1):
        if n[j]==n[j+1]:    #equal matches
            freq+=1
        elif n[j]<n[j+1]:    #increasing order
            freq=0
        if n[j]>n[j+1]:     #breaking case
            flag=1
            pos=j
            break

    if flag==1:
        for j in range(pos-freq+1,len(n)):
            n[j]='9'
        n[pos-freq]=int(n[pos-freq])-1
    output=("".join(map(str, n)).lstrip('0'))
    print("Case #{0}: ".format(i+1)+output)
    

        
