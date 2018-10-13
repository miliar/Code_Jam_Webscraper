import math
test = int(raw_input())
for n in range(1,test+1):
    x = raw_input()
    x = x[2:]
    x = x.split()
    o = 1
    b = 1
    time = 0
    ans = 0
    pre = 'x'
    for i in range(0,len(x),2):
        if(x[i] == 'B'):
            d = int(math.fabs(b-int(x[i+1])))
            if(pre == 'B' or pre == 'x'):
                time += d
                ans += d
            else:
                if(time < d):
                    ans += d-time
                    time = int(math.fabs(time-d))
                else:
                    time = 0
            b = int(x[i+1])
            pre = 'B'
            ans += 1
            time += 1
        if(x[i] == 'O'):
            d = int(math.fabs(o-int(x[i+1])))
            if(pre == 'O' or pre == 'x'):
                time += d
                ans += d
            else:
                if(time < d):
                    ans += d-time
                    time = int(math.fabs(time-d))
                else:
                    time = 0
            o = int(x[i+1])
            pre = 'O'
            ans += 1
            time += 1
        #print 'O = ' + str(o) + ' : B = ' + str(b) + ' : ans = ' + str(ans) + ' : time = ' + str(time)
    print 'Case #' + str(n) + ': ' + str(ans)
