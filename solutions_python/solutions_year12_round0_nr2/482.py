'''
Created on 14.04.2012

@author: Frederik Knust
'''
f = open('C:\Users\Freddy\Desktop\B-large.in')

o = open('C:\Users\Freddy\Desktop\ProblemB.out', 'w')

t = int(f.readline())

for i in range(t):
    l = f.readline()
    d = l.split(' ')
    n = int(d[0])
    s = int(d[1])
    p = int(d[2])
    g = []
    for j in range(n):
        g.append(int(d[3+j]))
        
    r = 0
    for tp in g:
        if tp == 0:
            if p == 0:
                r += 1
            continue
        
        if tp % 3 == 0:
            v = tp / 3
            if v >= p:
                # no surprise needed
                r += 1
            elif v + 1 >= p and s > 0:
                # surprise needed
                r += 1
                s -= 1
        else:
            v = tp / 3 + 1
            if v >= p:
                # no surprise needed
                r += 1
            elif v + 1 >= p and s > 0:
                # surprise needed, check if possible
                if v+1 + v-1 + v-1 == tp:
                    r += 1
                    s -= 1
            
    out = str.format('Case #{0}: {1}', i+1, r)
    print out
    o.write(out)
    o.write('\n')

f.close()
o.close()
    