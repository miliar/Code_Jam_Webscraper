import string

f=open("in.txt","r")
a=f.readlines()
f.close()

r=""
for i in xrange(1,len(a),2):
	r+="Case #"+str(i/2+1)+": "
	l=string.split(a[i])
	num=int(l[0])
	low=int(l[1])
	high=int(l[2])
	notes=string.split(a[i+1])
	notes=map(int,notes)
	notes.sort()
	notes.reverse()
	jnotes=range(low,high+1)
	for j in notes:
		jnotesp=jnotes+[]
		jnotes=[]
		for k in jnotesp:
			if k%j==0 or j%k==0:
				jnotes.append(k)
	try:
		r+=str(min(jnotes))
	except:
		r+="NO"
	r+="\n"

print r
f=open("out.txt","w")
f.write(r)
f.close()
