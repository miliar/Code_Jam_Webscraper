a="ejp mysljylc kd kxveddknmc re jsicpdrysi"
b="our language is impossible to understand"
x=dict()
for i in range(0,len(a)):
	x[a[i]]=b[i]
a="rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"
b="there are twenty six factorial possibilities"
y=dict()
for j in range(0,len(a)):
	y[a[j]]=b[j]
a="de kr kd eoya kw aej tysr re ujdr lkgc jv"
b="so it is okay if you want to just give up"
z=dict()
for k in range(0,len(a)):
	z[a[k]]=b[k]
final=dict(x.items()+y.items()+z.items())
final['q']='z'
final['z']='q'
#print(final)
#print(len(final))
test=int(raw_input())
for ran in range(0,test):
	a=raw_input()
	final_string=str()
	for l in range(0,len(a)):
		final_string+=final[a[l]]
	print("Case #"+str(ran+1)+": "+final_string)
