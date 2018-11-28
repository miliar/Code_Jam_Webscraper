import sys
d = { }
c = ["ejp mysljylc kd kxveddknmc re jsicpdrysi", 
    "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", 
    "de kr kd eoya kw aej tysr re ujdr lkgc jv"]
p = ["our language is impossible to understand", 
    "there are twenty six factorial possibilities", 
    "so it is okay if you want to just give up"]

for i in range(0, len(c)):
    cs = c[i]
    ps = p[i]
    for j in range(len(cs)):
        if cs[j] == ' ':
            continue
        else:
            d[cs[j]] = ps[j]

d['q'] = 'z'
d['z'] = 'q'

n = int(sys.stdin.readline().split()[0])
for i in range(0, n):
    cs = sys.stdin.readline()
    ds = ''
    for j in range(len(cs)):
        if cs[j] == ' ':
            ds = ds + ' '
        elif (ord(cs[j]) >= ord('a') and ord(cs[j]) <= ord('z')):
            ds = ds + d[cs[j]]
        else:
            break
    sys.stdout.write('Case #' + str(i+1) + ': ' + ds + '\n')
