a="ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv"
b="our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up"
dic={}
answer=[]
ans=[]
item=0
for x in a:
	if x!=" " and x not in dic:
		dic[x]=b[item]
	item+=1
dic["z"]="q"
dic["q"]="z"
f=open("1111.in", "r")
text=[]
text=f.readlines()
num=int(text[0])
m=0
g=1
while m!=int(num):
	result=""
	V=str(text[g])
	for x in V:
		if x in dic:
			result+=dic[x]
		else:
			result+=str(x)
	answer.append(result)
	m+=1
	g+=1
num=1
for x in answer:
	ans.append("Case #%s: %s" % (num, x))
	num+=1
f.close()
f=open("result.txt", "w")
f.writelines(ans)
f.close()


