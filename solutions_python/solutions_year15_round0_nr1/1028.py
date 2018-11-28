T = int(raw_input())
for i in range(T):
    r = 0
    m, s = raw_input().split()
    m = int(m)
    s = [int(j) for j in s]

    app = 0
    for pal in range(m):
        app += s[pal]
        if app<pal+1:
            app += 1
            r += 1

    print"Case #"+str(i+1)+": "+str(r)
