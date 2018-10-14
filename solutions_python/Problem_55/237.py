# coding: utf-8

"""
Theme Park
21:27 - 
"""
foutput  = open('C-small.out', 'w')

def coaster(k, groups, pos):
        passanger = 0
        first = groups[pos:]
        second = groups[:pos]
#        print str(first)
#        print str(second)
        for group in first:
                if (k - passanger) < group:
                        return pos, passanger
                passanger += group
                pos += 1
        pos = 0
        for group in second:
                if (k - passanger) < group:
                        return pos, passanger
                passanger += group
                pos += 1
        return pos, passanger
        
i = 0
for line in open('C-small.in', 'r'):
        i += 1
        items = map(int, line[:-1].split())
        if i == 1:
                continue
        if (i % 2) == 0:
                r = items.pop(0)
                k = items.pop(0)
                n = items.pop(0)
                continue
        groups = map(int, line[:-1].split())
#        print str(r) + ":" + str(k) + ":" + str(n) + ":" +str(groups)
        money = 0
        pos = 0
        for j in range(r):
                pos, passanger = coaster(k, groups, pos)
                money += passanger
        result = "Case #" + str(i // 2) + ": " + str(money) + '\n'
        print result,
        foutput.write(result)
foutput.close()
