n = int(input())
for i in range(n):
    c, f, x = map(float,raw_input().split(' '))
    t = 0
    g = 2.0
    while((x-c)/g > x/(g+f)):
        t += c/g
        g += f
    t += x/g
    print("Case #"+str(i+1)+": "+str(t))
