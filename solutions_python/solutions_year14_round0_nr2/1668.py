t = int(raw_input())
for test in range(1,t+1):
    c,f,x = map(float,raw_input().split(' '))
    rate = 2.0
    time = 0.0
    temptime = 0.0
    time = x/rate
    farms = 1
    temprate = rate
    for i in range(farms):
        temptime += c/temprate
        temprate += f
    temptime += x/temprate
    if(time < temptime):
        print 'Case #{}: {:.7f}'.format(test,time)
    else:
        while(temptime < time):
            time = temptime
            temptime = 0.0
            farms += 1
            temprate = rate
            for i in range(farms):
                temptime += c/temprate
                temprate += f
            temptime += x/temprate
        print 'Case #{}: {:.7f}'.format(test,time)
