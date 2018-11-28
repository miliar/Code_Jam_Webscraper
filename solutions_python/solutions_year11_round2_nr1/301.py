
f=open("in.txt","r")
a=f.readlines()
f.close()

class Team:
	winn=0
	losen=0
	oponentsi=[]
	oponentss=[]
	wp=0.0
	owp=0.0
	oowp=0.0
	rpi=0.0
	def __init__(self):
		self.winn=0
		self.losen=0
		self.oponentsi=[]
		self.oponentss=[]
		self.wp=0.0
		self.owp=0.0
		self.oowp=0.0
		self.rpi=0.0
	def computeWp(self):
		self.wp=float(self.winn)/(self.winn+self.losen)
	def computeRPI(self):
		 self.rpi = 0.25 * self.wp + 0.50 * self.owp + 0.25 * self.oowp

r=""
i=1
c=0
while c<int(a[0]):
	r+="Case #"+str(c+1)+":\n"
	num=int(a[i])
	teams=[]
	for j in a[i+1:i+num+1]:
		l=list(j.strip())
		t=Team()
		for k in xrange(len(l)):
			if l[k]=="0":
				t.losen+=1
				t.oponentsi.append(k)
				t.oponentss.append(0)
			elif l[k]=="1":
				t.winn+=1
				t.oponentsi.append(k)
				t.oponentss.append(1)
		t.computeWp()
		teams.append(t)
	for j in teams:
		sm=0.0
		for kk in xrange(len(j.oponentsi)):
			k=j.oponentsi[kk]
			s=teams[k].wp*len(teams[k].oponentsi)
			if j.oponentss[kk]==0:
				s-=1
			sm+=float(s)/(len(teams[k].oponentsi)-1)
		j.owp=sm/len(j.oponentsi)
	for jj in xrange(len(teams)):
		j=teams[jj]
		sm=0.0
		nn=0
		for k in j.oponentsi:
			if k!=j:
				sm+=teams[k].owp
			else:
				nn+=1
		j.oowp=sm/(len(j.oponentsi)-nn)
		j.computeRPI()
		r+=str(j.rpi)+"\n"
			
	i+=num+1
	c+=1
	
print r
f=open("out.txt","w")
f.write(r)
f.close()
	
