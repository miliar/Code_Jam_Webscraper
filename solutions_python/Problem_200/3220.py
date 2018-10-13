def believ(n):
    if len(n) == 1: return list(map(str, n))
    n = list(map(int, n))
    i = 1
    while(n[i-1] <= n[i]):
        i+=1;
        if (i == len(n)): return list(map(str, n));
    #we found something wrong.
    for y in range(i+1, len(n)):
        n[y] = 9
        
    while(i > 0 and n[i] - 1 < n[i-1]):
        n[i] = 9
        i-=1
    n[i] = n[i]-1
    return list(map(str, n))
        
for i in range(int(input())):
    print("Case #"+str(i+1)+": "+str(int("".join(believ(list(input()))))))
