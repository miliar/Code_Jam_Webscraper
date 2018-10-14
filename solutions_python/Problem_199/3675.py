T=int(input())
for q in range(T):
    S,K=map(str,input().strip().split(" "))
    S,K=[j for j in S],int(K)
    count=0
    for i in range(len(S)):
        if S[i]=='-':
            count+=1
            for l in range(K):
                if i+l<len(S):
                    if S[i+l]=='-':
                        S[i+l]='+'
                    elif S[i+l]=='+':
                        S[i+l]='-'
                else:
                    count=-1
                    break            
    if count==-1:
        print("Case #{}: {}".format(q+1,"IMPOSSIBLE"))
    else:
        print("Case #{}: {}".format(q+1,count))