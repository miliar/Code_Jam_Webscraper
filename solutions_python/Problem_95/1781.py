a = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc j"

b= "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up"
d = {}
d['a'] = 'y'
d['o'] = 'e'
d['z'] = 'q'
d['q'] = 'z'
for i in range(len(a)):
    print ord(a[i]), ord(b[i]), ord(b[i]) - ord(a[i])
    
    d[a[i]] = b[i]
for q in "abcdefghijklmnopqrstuvwxyz":
    if q not in d:
        print "haha"
        continue
    print d[q]
print sorted(d.values())
print d
f= open("A-small-attempt1.in", 'r')
t = f.readlines()
f.close()

cases = int(t[0])
o = open("1.out", 'w')
for c in range(1, cases+1):
    inp = t[c].strip()
    new = ''
    for l in inp:
        new += d[l]
    o.write("Case #" + str(c) + ": " + new + "\n")
o.close()
