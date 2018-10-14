# Problem A

c = []
c.append( "ejp mysljylc kd kxveddknmc re jsicpdrysi" )
c.append( "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd" )
c.append( "de kr kd eoya kw aej tysr re ujdr lkgc jv" )
p = []
p.append( "our language is impossible to understand" )
p.append( "there are twenty six factorial possibilities" )
p.append( "so it is okay if you want to just give up" )

d = {}
for i in range(3):
    for (x,y) in zip(c[i], p[i]):
        if not d.get(x):
            d[x] = y
        else:
            if d[x] != y:
                print ('FAIL', x, y, d[x])

d['z'] = 'q'
d['q'] = 'z'

l1 = [x for x in d.keys()]
l1.sort()
l2 = [x for x in d.values()]
l2.sort()

i = 1
l = []
lines = []
for line in open("A-small-attempt0.in"):
    lines.append(line.strip())
#print(lines)
for line in lines[1:]:
    for h in line:
        l.append(d[h])
    print ("Case #{i}: {s}".format(i=i, s=''.join(l)))
    l = []
    i += 1
