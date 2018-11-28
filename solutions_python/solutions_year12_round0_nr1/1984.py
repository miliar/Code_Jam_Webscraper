f = open('../data/1.txt','rb')
out = open('../data/1.out','wb')

d = {}

a = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv"
b = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up"

for i in range (0, len(a)):
    d[a[i]] = b[i]
d['y'] = 'a'
d['e'] = 'o'
d['q'] = 'z'
d['z'] = 'q'

C = int(f.readline())

for i in range(1, C+1):
    line = f.readline().strip()
    s = ""
    for c in line:
        
        s += d[c]
        
    out.write("Case #" + str(i) + ": " + s+"\n")    
    
