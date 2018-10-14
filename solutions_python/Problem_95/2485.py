

g1 = "ejp mysljylc kd kxveddknmc re jsicpdrysi"
g2 = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"
g3 = "de kr kd eoya kw aej tysr re ujdr lkgc jv"

t1 = "our language is impossible to understand"
t2 = "there are twenty six factorial possibilities"
t3 = "so it is okay if you want to just give up"

map1 = {}
for i in range(0, len(g1)):
    map1[g1[i]] = t1[i]

map2 = {}
for i in range(0,len(g2)):
    map2[g2[i]] = t2[i]

map3 = {}
for i in range(0, len(g3)):
    map3[g3[i]] = t3[i]

map = dict(map1, **map2)
map = dict(map, **map3)
map['q'] = 'z'
map['z'] = 'q'
with open('googlerese.in', 'r') as f:
    lines = f.read().split('\n')

T = int(lines[0])

case = 1
for line in lines[1:]:
    translated = ''
    for char in line:
        if map.has_key(char):
            translated += map[char]
        else:
            translated += char
    if case > T:
        break
    print "Case #%s: %s" %(case, translated)
    case += 1
