T = int(input())
i = 0
while i<T:
    i+=1
    s = [int(k) for k in input()]
    h = len(s)
    print("case #%i: "%i,end="")
    if h==1:
        print(s[0])
    else:
        j = h
        w = h-1
        while w>0:
            if(s[w]<s[w-1]):
                j = w
                s[w-1] -= 1
            w-=1
        if s[0]==0:
            w+=1
        while w<j:
            print(s[w],end="")
            w+=1
            pass
        while w<h:
            print(9,end="")
            w+=1
        print()
        
            
    
