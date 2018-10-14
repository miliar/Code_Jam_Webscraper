import string

s1 = "qzejp mysljylc kd kxveddknmc re jsicpdrysi \
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd \
de kr kd eoya kw aej tysr re ujdr lkgc jv"

s2 = "zqour language is impossible to understand \
there are twenty six factorial possibilities \
so it is okay if you want to just give up"

tr = string.maketrans(s1, s2)

with open('tongues.txt') as f, open('out.txt', 'w') as g:
    n = int(f.readline())
    for _ in range(n):
        s = 'Case #' + str(_+1) + ': ' + f.readline().translate(tr)
        g.write(s)
        
    
