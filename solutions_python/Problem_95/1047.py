s='ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jvzq'
s2='our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give upqz'
def tr(s,s2,text):
	res=''
	for x in text:
		res+=s2[s.find(x)]
	return res

file = open('a.in','r')

t=int(file.readline())
ret=[]
for x in file.readlines():
	x=x.replace('\n','')
	x=x.replace('\r','')
	ret.append(tr(s,s2,x))
file2=open('a.out','w')
for x in range(len(ret)):
	file2.write('Case #'+str(x+1)+': '+ret[x]+'\n')
file2.close()
file.close()

