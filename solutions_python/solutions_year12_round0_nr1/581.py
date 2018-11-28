l = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv"
k = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up"
d = {}
for i in range(0,len(l)):
    d[l[i]] = k[i]
#q and z are not there in either of k and l.We know that z maps to q,so q must map to z.#
d["z"] = "q"
d["q"] = "z"
fh = open("a.in",'r')
fhw = open("b.txt",'w')
f = fh.readlines()
x1 = f[0].strip()
x = int(x1)
y1 = f[1:]
i = 0
d1 = {}
while i < x:
    for t in y1:
        y = t.strip()
        for j in range(0,len(y)):
            y = y[:j] + d[y[j]] + y[(j + 1):]
        if i != (x - 1):
            d1[i] ="Case #" + str((i + 1)) +": " + y + "\n"
        else:
            d1[i] ="Case #" + str((i+1)) +": " + y
        i = i + 1
for u in range(0,x):
    fhw.write(d1[u])
fh.close()
fhw.close()
