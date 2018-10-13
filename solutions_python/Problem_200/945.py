#/usr/bin/python3



def solve(N):
    N = list(N)
    res = ""
    prev = 0
    while N:
        act = int(N.pop(0))
        #print(prev, act)
        if prev <= act:
            res += str(prev)
            prev = act
        else:
            res += str(prev-1)
            res += "9"*len(N)
            prev = 9
            break
    res += str(prev)
    return str(int(res))
    


T = int(input())

for t in range(T):
    
    N = input()
    
    while True:
        M = solve(N)
        if M == N:
            break
        else:
            N = M
    
    print("Case #{0}: {1}".format(t+1, int(N)))


