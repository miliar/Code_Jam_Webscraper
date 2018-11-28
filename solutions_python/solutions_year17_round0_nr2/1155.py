noTests=int(input())
for i in range(1,noTests+1):
    List=list(input().strip())
    length=len(List)
    List.insert(0,'-1')
    b=['' for _ in range(length+1)]
    for j in range(length,0,-1):
        if List[j-1]<=List[j]:
            b[j]=List[j]
        else:
            List[j-1]=chr(ord(List[j-1])-1)
            k=j
            while k<=length:
                
                b[k]='9'
                try:
                    if b[k+1]=='9':
                        break
                except:
                    break
                k+=1
    b=''.join(b)
    print("Case #{}: {}".format(i,int(b)))
