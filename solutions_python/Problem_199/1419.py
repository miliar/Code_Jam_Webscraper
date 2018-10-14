T = int(input())

def flip(s):
    if s == '+':
        return '-'
    return '+'

for t in range(T):
    s, k = input().split()

    s = list(s)
    n = len(s)    
    k = int(k)
    c = 0
    for i in range(n-k+1):
        if s[i] == '-':
            c += 1
            for j in range(k):
                s[i+j] = flip(s[i+j])
        
    
    for i in range(n):
        if s[i] != '+':
            c = -1
    #print(s)        
    print("Case #{}: {}".format(t+1, c if c>=0 else "IMPOSSIBLE"))