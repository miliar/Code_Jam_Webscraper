best = 0

def rec(n,i):
    global best
    global N
    if n > int(N[:i]) or (len(N)-i > 0 and n*(10**(len(N)-i))+int(''.join(['9']*(len(N)-i))) <= best):
        return
    if n <= int(N) and n>best:
        best=n
    if(i==len(N)):
        return

    for j in range(9,(n%10)-1,-1):
        rec(n*10+j,i+1)


T = int(input())
for t in range(1,T+1):
    best = 1
    N=input()
    for i in range(int(N[0]),-1,-1):
        rec(i,1)
    print("Case #%d: %d" % (t,best))


