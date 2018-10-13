
f = open("D-large.in")
out = open("output.txt", "w")
T = int(f.readline())

for t in range(T):
    s = ["Case #%d:" %(t+1)]
    n = int(f.readline())
    ken = [[x, True] for x in f.readline().split(" ")]
    naomi = [[x, True] for x in f.readline().split(" ")]
    
    ken.sort()
    naomi.sort()
    
    ans = 0
    for x in ken:
        for i, y in enumerate(naomi):
            if x[0] > y[0] and y[1]:
                naomi[i][1] = False
                ans += 1
                break
    s.append(str(ans))
    ans = 0
    for x in naomi:
        for i, y in enumerate(ken):
            if x[0] > y[0] and y[1]:
                ken[i][1] = False
                ans += 1
                break
    s.append(str(n-ans))
    out.write(" ".join(s) + "\n")
    

    