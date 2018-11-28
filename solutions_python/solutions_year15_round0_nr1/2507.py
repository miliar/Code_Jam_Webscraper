

t=int(input())
c=1
while c<=t:
    r=input().split()
    
    ppl=list(r[1])
    ppl=[int(x) for x in ppl]
    stand=0
    need=0
    for x in range(int(r[0])+1):
        if stand >= x:
            stand+=ppl[x]
        else:
            need+=x-stand
            stand+=(x-stand)+ppl[x]

    print("Case #{}: {}".format(c,need))
    c+=1
