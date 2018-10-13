def tobin(x):
    global nn
    ret = ''
    while(x != 0):
        ret += str(x%2)
        x /= 2
    while(len(ret) < nn):
        ret += '0'
    ret = ret[::-1]
    return ret

def xor(x,y):
    ret = ''
    for i in range(nn):
        if(x[i] == y[i]):
            ret += '0'
        else:
            ret += '1'
    return ret
    

test = int(raw_input())
for n in range(1,test+1):
    k = int(raw_input())
    x = raw_input().split()
    xx = []
    for i in x:
        xx.append(int(i))
    xx.sort()
    nn = 0
    while(xx[len(xx)-1] >= 2**nn):
        nn += 1
    lis = []
    for i in xx:
        lis.append(tobin(i))
    res = ''
    for i in range(nn):
        res += '0'
    for i in lis:
        res = xor(res,i)
    if('1' in res):
        ans = 'NO'
    else:
        ans = 0
        for i in xx:
            ans += i
        ans -= xx[0]
        ans = str(ans)
    print 'Case #' + str(n) + ': ' + ans
