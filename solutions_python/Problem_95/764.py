a = ["ejp mysljylc kd kxveddknmc re jsicpdrysi",
"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
"de kr kd eoya kw aej tysr re ujdr lkgc jv"]

b = ["our language is impossible to understand",
"there are twenty six factorial possibilities",
"so it is okay if you want to just give up"]

tlum = {}
a = "".join(a)
b = "".join(b)

for i in range(len(a)):
	tlum[a[i]] = b[i]

tlum['q']='z'
tlum['z']='q'
tlum['y']='a'
tlum['e']='o'
n = int(raw_input())
for i in range(n):
	S = raw_input()
	S = "".join(map(lambda x:tlum[x],S))
	print "Case #%d: %s"%(i+1,S)
