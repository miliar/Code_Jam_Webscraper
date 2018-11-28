import time
t = time.clock()
#f = open('Cookie-Test.txt')
#f = open('Cookie-Small.txt')
f = open('Cookie-Large.txt')
#out = open('Cookie-Test-Out.txt','w+')
#out = open('Cookie-Small-Out-t.txt','w+')
out = open('Cookie-Large-Out.txt','w+')

def func(caseI,gen):
    C,F,X = [float(f) for f in gen.next().split(' ')[:3]]
    total = 0
    R = X/C
    genC = nextCRate(C,F)
    currentC = genC.next()
    nC = genC.next()
    while (currentC / R) + nC < currentC :
        total += currentC
        currentC = nC
        nC = genC.next()
    total += currentC * R
    v = "{0:.7f}".format(total)
    return 'Case #' + str(caseI+1)+": " + v

def nextCRate(C,F):
    rate = 2
    while True:
        yield C/rate
        rate += F

lines = f.read().split('\n')
cases = int(lines[0])
gen = (l for l in lines[1:])
for i in range(cases):
    out.write(func(i,gen)+'\n')
f.close()
out.close()

print time.clock() - t
