english = []
googlerese = []

e=[]
g=[]

e.append("a zoo")
g.append("y qee")

e.append("our language is impossible to understand")
g.append("ejp mysljylc kd kxveddknmc re jsicpdrysi")

e.append("there are twenty six factorial possibilities")
g.append("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd")

e.append("so it is okay if you want to just give up")
g.append("de kr kd eoya kw aej tysr re ujdr lkgc jv")

alphabet="qwertyuiopasdfghjklzxcvbnm "

for i in range(len(e)):
    a=list(e[i])
    b=list(g[i])
    for j in range(len(a)):
        if a[j] not in english:
            english.append(a[j])
            googlerese.append(b[j])

if len(english)+1==len(alphabet):
    for i in alphabet:
        if i not in english:
            english.append(i)
        if i not in googlerese:
            googlerese.append(i)

a=open("A0.in")
b=a.readlines()

for i in range(int(b[0])):
    res=""
    c=str(b[i+1])
    if c[-1:]=="\n":
        c=c[:-1]
    for k in c:
        res+=english[googlerese.index(k)]

    
    print "Case #"+str(i+1)+": "+res
