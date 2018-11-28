def solve():
    a = input().rstrip()
    n = [int(e) for e in a]
    for j in range(1,len(n)):
        if n[j-1] > n[j]:
            for k in range(j-1, 0, -1 ):
                if n[k-1] <= n[k] - 1:
                    n[k]-= 1
                    n[k+1:len(n)]=[9 for e in range(len(n) -k-1)]
                    return "".join(str(e) for e in n)

            n[0]-=1
            n[1:len(n)]=[9 for e in range(len(n) -1)]
            return str(int("".join(str(e) for e in n[0:len(n)])))
    return "".join(str(e) for e in n)

    
T=int(input())
 
for t in range(1,T+1):
    print ("Case #" + str(t) + ": " + solve())
