import string

f = open("A-large.in", 'r', 0)
fout = open("A_res.in", "w")
T = int(f.readline().split()[0])

def foldsum(a, n):
    if n == 0:
        return a
    return foldsum(2*a-1, n-1)

for t in xrange(T):
    A, N = map(int, f.readline().split())
    L = map(int, f.readline().split())
    L.sort()
    C = [A]
    R = 0
    n = 0
    AC = []
    temp = 0
    after = 0
    
    while n != len(L):
        if C[n] == 1:
            R += 1
            C.insert(n+1, C[n])
            AC.insert(n,0)
        elif L[n] >= C[n]:
            temp += 1
            C.insert(n+1, C[n]+C[n]-1)
            L.insert(n, C[n]-1)
            if C[n+1] > L[n+1]:
                AC.insert(n, temp)
                temp = 0
                after = 1
        else:
            C.insert(n+1, C[n]+L[n])
            if after == 0:
                AC.insert(n,0)
            if after == 1:
                after = 0
        n += 1

    for i in range(1,len(AC)+1):
        while sum(AC[-i:len(AC)]) > len(AC[-i:len(AC)]):
            AC[-i] -= 1
    R += sum(AC)
    print("Case #" + str(t+1) + ": " + str(R))
    fout.write("Case #" + str(t+1) + ": " + str(R) + "\n")
fout.close()
