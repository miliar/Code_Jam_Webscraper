def tidy(n):
    for i in range(n, -1, -1):
        if check(i):
            return str(i)

def tidy2(n):
    l = list(str(n))
    if not check(n):

        last =-1
        for x in range(0, len(l) - 1):
            if l[x+1] < l[x]:

                if x > 0 and int(l[x])-1 < int(l[x-1]):
                    zt = int(l[x])-1
                    for z in range(0, len(l) - 1):
                        if zt < int(l[z]):
                            t = int(l[z])-1
                            l[z]=t
                            last=z
                            break
                else:
                    t = int(l[x]) - 1
                    l[x] = t
                    last = x
                break

        for x in range(last+1, len(l)) :
            l[x]='9'

    return ''.join(map(m1,l))

def m1(n):
    if n!=0:
        return str(n)
    return ''

def n2(n):
    l = list(str(n))
    last = -1
    for x in range(0, len(l) - 1):
        if l[x + 1] < l[x]:
            t = int(l[x]) - 1
            l[x] = t
            last = x
            break

    for x in range(last, 0, -1):
        if l[x+1] < l[x]:
            return True

    return False

def check(i):
    l = list(str(i))

    for x in range(0, len(l)-1):
        if l[x] > l[x + 1]:
            return False

    return True

def test():
    print(tidy2(111111111111111110000000))

    for i in range(1,1000):
        if tidy(i) != tidy2(i):
            print(i,tidy(i), tidy2(i))

def readFile():
    f1 = open('B-large.in', 'r')

    n = int(f1.readline())
    #w = temp.rstrip('\n')
    l = []

    for i in range(1,n+1):
        t = int(f1.readline())
        l.append(t)

    return l

l = readFile()

for i in range(1, len(l)+1):
    print('Case #'+ str(i)+ ':', tidy2(l[i-1]))