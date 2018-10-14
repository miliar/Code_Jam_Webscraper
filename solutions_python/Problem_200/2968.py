T = int(input())
for t in range(1,T+1):
    n = input()
    s = ""
    for i in range(len(n)-1):
        if n[i] > n[i+1]:
            k = i
            for j in range(i, -1, -1):
                if n[i] == n[j]:
                    k = j
                else:
                    break
            s = n[:k]
            for j in range(k, i+1):
                if j > 0 and k != i:
                    s += '9'
                else:
                    s += str((int(n[i])-1)%10)
            s += '9'*(len(n)-i-1)
            break
    if not s:
        s = n
    print("Case #%d: %d" %(t, int(s)))

