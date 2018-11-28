t={}
d="abcdefghijklmnopqrstuvwxyz"
i=0
for ch in "ynficwlbkuomxsevzpdrjgthaq":
    t[ch]=d[i]
    i+=1
i=0
f=open("a.in")
g=open("a.out","w")
for line in f.readlines()[1:]:
    i+=1
    g.write("Case #"+str(i)+": ")
    for ch in line:
        if ch >= 'a' and ch <= 'z':
            ch=t[ch]
        g.write(ch)
g.close()
