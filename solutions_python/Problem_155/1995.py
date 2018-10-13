import sys
DEBUG = True

if DEBUG:
    filename = 'input.in'
else:
    filename = None

if filename:
    inf = open(filename)
else:
    inf = sys.stdin

T = inf.readline()

def sol(t):
    t = t.split()
    max_shy, audience = t[0], t[1]
    ovators = 0
    to_add = 0
    i = 0
    while i <= int(max_shy):
        member = audience[i]
        if ovators >= i:
            ovators += int(member)
            i += 1
        else:
            to_add += 1
            ovators += 1
    return to_add
            
            
            
    return t

for i in range(int(T)):
    test = inf.readline()
    test = test.strip()
    print("Case #%d: " % (i+1) + str(sol(test)))

if inf is not sys.stdin:
    inf.close()
