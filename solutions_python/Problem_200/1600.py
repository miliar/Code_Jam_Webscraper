t = int(input())
numbers = [input() for x in range(t)]

for n in range(t):
    
    nlist = [int(c) for c in str(numbers[n])]
    
    changed = True
    while (changed):
        
        changed = False
        
        for i in range(len(nlist)-1):
            if nlist[i]>nlist[i+1]:
                nlist[i] -= 1
                nlist = nlist[:i+1] + [9] * (len(nlist) - i -1)
                changed = True
    
    res = ''.join(str(x) for x in nlist)
    
    print("Case #{}: {}".format(n+1, int(res)))
        
