def solve(N):
    desceding = False
    for i in range(len(str(N))-1):
        if str(N)[i] > str(N)[i+1]:
           desceding = True
    if desceding:
        return solve(N-1)
    else:
        return N


T = int(input())
for i in range(T):
    N = int(input())
    number = solve(N)
    print("Case #"+str(i+1)+': '+str(number))
