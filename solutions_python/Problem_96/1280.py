


f = open("p2.in","r")
g = open("p2.out","w")

nrt = int(f.readline().strip())

for test in range(1,nrt + 1):
    aux = f.readline().strip().split()
    n = int(aux[0])
    s = int(aux[1])
    p = int(aux[2])
    ans = 0
    for i in range(0,n):
        total = int(aux[3 + i ])
        if total / 3 >= p:
            ans += 1
            continue
        if total % 3 >= 1:
            if total / 3 + 1 >= p:
                ans +=1
                continue
        if total % 3 == 0:
            if total != 0 and total / 3 + 1 >= p and s > 0:
                ans += 1
                s -=1 
                continue
        if total % 3 == 2:
            if total / 3 + 2 >= p and s > 0:
                ans += 1
                s -= 1
                continue
    g.write("Case #" +str(test) + ": " + str(ans) + "\n")

            



