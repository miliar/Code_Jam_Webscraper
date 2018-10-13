def solve():
    a,b= [e for e in input().split()]
    lis = list(a)
    k = int(b)
    count=0
    for n in range(len(lis)-k+1):
        if lis[n] == '-':
            lis[n:n+k]=[flip(e) for e in lis[n:n+k]]
            count+=1
    if lis != list(len(lis)*'+'):
        return "IMPOSSIBLE"
    return str(count)
            
def flip(s):
    if s == '+':
        return '-'
    else:
        return '+'


T=int(input());
 
for t in range(1,T+1):
    print ("Case #" + str(t) + ": " + solve())
