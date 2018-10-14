'''
Created on 14.04.2012

@author: Frederik Knust
'''

f = open('C:\Users\Freddy\Desktop\C-large.in')
o = open('C:\Users\Freddy\Desktop\ProblemC.out', 'w')

t = int(f.readline())

for i in range(t):
    l = f.readline()
    d = l.split(' ')
    minValue = int(d[0])
    maxValue = int(d[1])
    r = 0
    p = set()
    
    for v in range(minValue, maxValue+1, 1):
        vs = str(v)
        va = map(str, vs)
        
        for j in range(len(va)-1):
            va.insert(0, va.pop())
            vs = ''.join(va)
            newv = int(vs)
            if newv > v and newv <= maxValue:
                if (v, newv) not in p:
                    r += 1
                    p.add((v, newv))
    
    out = str.format('Case #{0}: {1}', i+1, r)
    print out
    o.write(out)
    o.write('\n')

f.close()
o.close()
