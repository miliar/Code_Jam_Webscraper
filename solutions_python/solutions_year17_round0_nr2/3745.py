def isTidy(num) :
    A = list(str(num))
    B = A[:]
    B.sort()
    return (A == B)

T = int(input())
for k in range (1, T+1) :
    N = int(input())
    for i in range (N, 0, -1) :
        if isTidy(i) :
            print("Case #", k, ": ", i, sep = "")
            break
