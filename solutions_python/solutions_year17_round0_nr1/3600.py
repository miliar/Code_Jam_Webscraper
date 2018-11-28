

t = int(input())

for j in range(t):
    line = raw_input().strip()
    t,k = line.split(" ")
    k = int(k)
    t = list(t)
    jj = 0
    change = 0
    while jj<len(t):
        if t[jj]=="-" and jj+k<=len(t):
            change +=1
            for i in range(k):
                t[jj+i] = "+" if t[jj+i]=="-" else "-"
        jj+=1
    if all([k=="+" for k in t]):
        print("Case #%d: %s"%(j+1,change))
    else:
        print("Case #%d: %s"%(j+1,"IMPOSSIBLE"))