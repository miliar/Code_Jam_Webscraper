t = input()
for i in range(t):
    c,f,x = map(float, raw_input().split())
    d = 2.0
    time = 0
    y = "Case #"+str(i+1)+":"
    if x<c:
        print y,("%.7f")%(x/d)
    else:
        while x/d>(c/d+(x/(f+d))):
            time+=c/d
            d = d+f
        time+=x/d
        print y,("%.7f")%time
