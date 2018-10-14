def sieve(a,b):
    return [False for i in xrange(b+1)]

def recycled(n):
    x = str(n)
    temp = []
    if len(set(list(x))) != 1: 
        temp.append(x)
    for i in range(len(x)-1):
        new = x[i+1:]+x[:i+1]
        if new[0] == '0':
            continue
        if len(set(list(new))) == 1:
               continue
        if new not in temp:
            temp.append(new)
    return temp

def count_recycled(a,b):
    total = 0
    answers = sieve(a,b)
    for i in range(a,b+1):
        count = 0
        temp = recycled(i)
        if len(temp) == 1:
            continue
        for j in temp:
            v = int(j)
            if v >= a and v <= b:
                if not answers[v]:
                    answers[v] = True
                    count += 1
        total += (count**2-count)//2

    return total

f = open('Google Recycled Numbers.in','r')
g = open('Google Recycled Numbers.out','w')

cases = int(f.readline())

for i in range(cases):
    line = f.readline().rstrip()
    line = line.split(' ')
    line = [int(p) for p in line]
    a = line[0]
    b = line[1]
    value = str(count_recycled(a,b))
    g.write("Case #%s: %s\n" %(str(i+1),value))
g.close()
f.close()
print "Done."

    
    
