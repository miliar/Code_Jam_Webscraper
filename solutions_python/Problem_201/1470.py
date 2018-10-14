import math
t = int(raw_input(''))
for i in range(t):
    tc = raw_input('')
    tc = tc.split(' ')
    n = int(tc[0])
    k = int(tc[1])
    p = math.log(k,2)
    in1 = int(p)
    q = 2**in1
    div = float((n-q+1))/q
    in2 = int(div)
    dec = div - in2
    dec = int(dec*q)
    dec1 = k - q
    if(dec >dec1):
        x = math.ceil(div)
    else:
        x = math.floor(div)
    if x == 0:
        print 'Case #' + str(int(i + 1)) + ': 0 0' + '       '+str(x)
    elif x%2 == 0:
        print 'Case #' + str(int(i + 1)) + ': ' + str(int(x/2)) + ' ' + str(int((x/2 )-1)) 
    else:
        print 'Case #' + str(int(i + 1)) + ': ' + str(int(x/2)) + ' ' + str(int(x/2))
