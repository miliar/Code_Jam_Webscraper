f1 = open("B-small-attempt2.in", "r")
t = int(f1.readline().split('\n')[0])
for i in range(t):
    n = int(f1.readline().split('\n')[0])
    l = []
    temp = 10
    k = 1
    while n > 0:
        if n%10 == 0 and k == 1:
            n -= 1
        else:
            r1 = n%10
            r2 = int(n/10)%10
            if r1 < r2:
                if l:
                    l = []
                    n = temp
                n -= 1
            else:
                l.append(r1)
                temp = n
                n=int(n/10)
        k += 1
    l.sort()
    l = list(map(str, l))
    f2 = open("output.txt", "a")
    f2.write("Case #"+str(i+1)+": "+"".join(l))
    f2.write("\n")
    f2.close()
