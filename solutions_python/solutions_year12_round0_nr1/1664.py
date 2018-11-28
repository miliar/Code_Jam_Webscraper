exinp = """ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv
y qee z"""

exout = """our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up
a zoo q"""

key = {}
for i in range(len(exinp)):
	key[exinp[i]]=exout[i]

#for i,j in key.items():
#	print(i+"="+j)

f = open("A-small-attempt0.in","r")
n = int(f.readline())
out=""
for i in range(n):
	s = f.readline()
	prnt = "Case #"+str(i+1)+": "
	for j in s:
		prnt+=key[j]
	print(prnt.strip())
	out+=prnt.strip()+"\n"
f.close()
f = open("out.txt","w")
f.write(out)
f.close()