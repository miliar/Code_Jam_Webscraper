import string

f=open("in.txt","r")
a=f.readlines()
f.close()

r=""
i=1
c=0
while c<int(a[0]):
	r+="Case #"+str(c+1)+":\n"
	h=int(string.split(a[i])[0])
	w=int(string.split(a[i])[1])
	i+=1
	b=[]
	for j in xrange(i,i+h):
		b.append(list(a[j].strip()))
	impossible=False
	for x in xrange(w):
		for y in xrange(h):
			if b[y][x]=='#':
				try:
					if b[y][x+1]=='#' and b[y+1][x]=='#' and b[y+1][x+1]=='#':
						b[y][x]="/";b[y][x+1]="\\";b[y+1][x]="\\";b[y+1][x+1]="/"
					else:
						impossible=True
				except:
					impossible=True
	i+=h
	c+=1
	if impossible:
		r+="Impossible\n"
	else:
		for j in b:
			r+=string.join(j,"")+"\n"

print r
f=open("out.txt","w")
f.write(r)
f.close()
