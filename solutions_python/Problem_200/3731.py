n = int(input())

def is_tidy(x):
    x = str(x)
    l = len(x)
    for i in range(0,l-1):
        if(x[i] == '0'):
            return False
        elif(x[i]>x[i+1]):
            return False
    return True

def make(y):
    y = str(y)
    l = len(y)
    global ret
    for i in range(0,l-1):
        if(y[i]>y[i+1]):
            ret = y[0:i]
            a = int(y[i])-1
            ret = ret + str(a)
            for k in range(i+1,l):
                ret += '9'
    return int(ret)

for i in range(1, n + 1):
    num = int(input())
    j = num
    while(j>=0):
        if(is_tidy(j)):
            break
        else:
            j = make(j)
            #print("Processing",j)
    print("Case #%d: %d" %(i,j))
