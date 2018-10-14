# cook your dish here
t = int(input())
j = 0
for k in range(t):
    n = list(map(int, input()))
    if(sorted(n) == n):
        m = int(''.join(map(str, n)))
    else:
        for i in range(len(n)-1):
            j=0
            if(n[i] >= n[i+1]):
                n[i] = n[i] - 1
                break
        for j in range(i+1, len(n)):
            n[j] = 9
        m = int(''.join(map(str, n)))
    print("Case #%d: %d" %((k+1),m))


