import time
t = time.clock()
#f = open('Elf-Test.txt')
f = open('Elf-Small.txt')
#f = open('Elf-Large.txt')
#out = open('Elf-Test-Out.txt','w+')
out = open('Elf-Small-Out.txt','w+')
#out = open('Elf-Large-Out.txt','w+')

def func(caseI,gen):
    P,Q = [int(f) for f in gen.next().split('/')[:2]]
    total = rec(P,Q,0)
    return 'Case #' + str(caseI+1)+": " + str(total)

def rec(P,Q,T):
    if P-Q == 0:
        return T
    if P-Q > 0:
        if rec(P-Q,Q,T+1) == "impossible":
            return "impossible"
        return T
    if T > 40:
        return "impossible"
    P,Q = red(P*2,Q)
    return rec(P,Q,T+1)

def red(P,Q):
    LCD = 2
    while P % LCD != 0 or Q % LCD != 0:
        if LCD > Q /2:
            return P,Q
        LCD += 1
    return P/LCD, Q/LCD

lines = f.read().split('\n')
cases = int(lines[0])
gen = (l for l in lines[1:])
for i in range(cases):
    out.write(func(i,gen)+'\n')
f.close()
out.close()

print time.clock() - t
