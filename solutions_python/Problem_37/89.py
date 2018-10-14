f = open('A-small-attempt1.in')
of = open('result.txt','w')

def toBaseSum(n,b):
    res = []

    while n != 0:
        res.append(n%b)
        n = n / b

    s = 0
    for x in res:
        s = s + int(x)**2

    return s

def isHappy(n, b):
    hist = []

    r = n
    
    while 1:
        r = toBaseSum(r, b)

        if r == 1:
            return 1
        elif hist.count(r) == 0:
            hist.append(r)
        else:
            return 0
    
def oper(b):
    pass

def main():
    line = int(f.readline())
    
    for x in range(line):
        bases = f.readline().split()
        bases.reverse()

        n = 2
        isFind = 0
        result = 0

        while 1:
            tonext = 0
            for y in bases:
                if not isHappy(n, int(y)):
                    n = n + 1
                    tonext = 1
                    break

            if tonext == 0: break

        of.write('Case #'+str(x+1)+': '+str(n)+'\n')

if __name__ == '__main__':
    main()

f.close()
of.close()


