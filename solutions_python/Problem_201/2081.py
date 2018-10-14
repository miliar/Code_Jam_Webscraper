n=int(input())
input_=[]
def go(metres,k):
    if metres[0]==k:
        return 0
    for i in range(k-1):
        metres.sort()
        bufer=metres[len(metres)-1]
        if metres[len(metres)-1]%2==0:
            metres[len(metres)-1]=bufer//2
            metres.append((bufer//2)-1)
        else:
            metres[len(metres)-1]=bufer//2
            metres.append(bufer//2)
    metres.sort()
    return metres[len(metres)-1]
for i in range(n):
    input_.append([int(i) for i in (input().split())])
for i in range(len(input_)):
    metres=[]
    metres.append(input_[i][0])
    result=go(metres,input_[i][1])
    max_=result//2
    if max_==0:
        min_=0
    elif result%2==1:
        min_=max_
    else:
        min_=max_-1
    print("Case #%d: %d %d" % (i+1, max_, min_))
    
    
    
    
