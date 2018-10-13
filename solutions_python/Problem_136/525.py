repeat = int(input())
for i in range(repeat):
    result = 0.0
    cookies = 0.0
    farms = 0.0
    o = 2.0
    c,f,x = (float(a) for a in input().split(" "))
    if x <= c:
        result = x/o
    else:
        flag = True
        while flag:
            cookies += c
            result += c/(o+farms*f)
            if (x-cookies+c)/(o+(farms+1.0)*f) * f > c:
                cookies -= c
                farms += 1.0
            else:
                result += (x-cookies)/(o+farms*f)
                flag = False
    print("Case #"+str(i+1)+": "+str(float('%.7f' % result)))