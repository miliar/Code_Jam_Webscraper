t = int(input())

for i in range(t):
    n = input()
    n = list(n)
    for k in range(0,len(n)-1):
        if n[k] > n[k+1]:
            for j in range(k+1,len(n)):
                n[j]='9'
            n[k]=chr(ord(n[k])-1)
            j = k
            while j>0 and n[j] < n[j-1]:
                n[j] ='9'
                n[j-1] = chr(ord(n[j-1])-1)
                j-=1
            break

    while n[0] == '0':
        n.pop(0)
    print("Case #{}: {}".format(i+1,''.join(n)))