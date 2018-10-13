fob = open('c:/test/c.txt','r')
test = fob.readline()
test = int(test)

def rotator(n):
    if n == 0:
        return 0
    t = str(n)
    t = list(t)
    i = t.pop(0)
    t.append(i)
    if t[0] == '0':
            t = ''.join(t)
            return rotator(t)
    else :
            t = ''.join(t)
            t = int(t)
            return t

i = 0
while i < test:
    line = fob.readline()
    line = line.split()
    a = line[0]
    a = int(a)
    b = line[1]
    b = int(b)
    total = 0
    
    j = a
    while j<=b:
        t = rotator(j)
        while t != j:
            if t <= b and t >= a:
                total += 1
                #print t
            t = rotator(t)
        j += 1
    total = total/2
    print 'Case #'+`i+1`+': '+ `total`
    i += 1
fob.close()
