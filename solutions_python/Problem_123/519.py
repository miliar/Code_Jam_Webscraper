import sys

best = 10**10

def calc(a, motes, sofar):
    global best
    
    # shortcut
    if sofar > best:
        return sofar
    
    if motes == []:
        return sofar
    
    first = motes[0]
    rest = motes[1:]
    
    if first < a:
        return calc(a+first, rest, sofar)
    else:
        removeCost = calc(a, rest, sofar+1)
        addCost = calc(a + a -1, motes, sofar+1)
        
        return min(removeCost, addCost)


f = sys.stdin

count = int(f.readline())

for index in range(1, count+1):
    (a, n) = map(int, f.readline().split(" ", 2))
    motes = map(int, f.readline().split(" "))
    #print("{} {} {}".format(a, n, motes))
    motes.sort()
    best = len(motes)   # can always remove all
    cost = calc(a, motes, 0)
    print("Case #{}: {}".format(index, cost))
