fin = open("C.in")
fout = open("C.out", "w")
T = int(fin.readline())

def done(t, n1, n2):
    fout.write("Case #"+str(t+1) + ": " + str(n1) + " " + str(n2) + "\n")

def even(n):
    return n%2 == 0

for t in range(T):
    N, K = map(int, fin.readline().split())
    while K > 1:
        if even(N):
            if even(K):
                N = N // 2
                K = K // 2
            else:
                N = N // 2 -1
                K = K // 2
        else:
            N = N // 2
            K = K // 2
    if even(N):
        done(t, N//2, N//2-1)
    else:
        done(t, N//2, N//2)

        
