
t = int(input())
for i in range(1, t+1):
    n = 0
    s, k = input().split()
    k = int(k)
    l = [False] * len(s)
    for j in range(len(s)): 
        if s[j] == '+':
            l[j] = True
    
    for j in range(len(s)- k + 1):
        if not l[j]:
            l[j:j+k] = [not x for x in l[j:j+k]]
            n = n+1
    
    if not all(l):
        n = "IMPOSSIBLE"
     
    
    print("Case #{}: {}".format(i, n))