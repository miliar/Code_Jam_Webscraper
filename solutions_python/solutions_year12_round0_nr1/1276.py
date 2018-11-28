from string import maketrans 
intab = "qzour language is impossible to understand\nthere are twenty six factorial possibilities\nso it is okay if you want to just give up"
outtab = "zqejp mysljylc kd kxveddknmc re jsicpdrysi\nrbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd\nde kr kd eoya kw aej tysr re ujdr lkgc jv"
trantab = maketrans(outtab, intab)
f=open("lalaa.txt","r")
pika=f.read()
kska=pika.split("\n")
kska.pop(0)
print kska
lala=pika.split()
T=int(lala.pop(0))
pika=list(pika)
pika.pop(0)
pika.pop(0)
pika.pop(0)
o=0
while T!=0:
        o=o+1
        T=T-1
	q=open("respgoo.txt","a")
        q.write("Case #"+str(o)+": "+str(kska[o-1].translate(trantab))+"\n")

