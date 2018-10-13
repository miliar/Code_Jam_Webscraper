t = int(input())
for i in range(t):
    a,b = map(int,input().split())
    ini = 0
    speed = 0
    t_ini = 0
    t_speed = 0
    foo = 1
    maxi = 0
    for j in range(b):
        t_ini,t_speed = map(int,input().split())
        if(((a-t_ini)/t_speed) > maxi ):
            foo = (a-t_ini)/t_speed
            maxi = foo
    print("Case ","#",i+1," {0:.6f}".format(a/foo),sep='')
        
