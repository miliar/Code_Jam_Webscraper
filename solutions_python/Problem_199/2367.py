
def readinput():
	global t
	global inp
	i=0
	for line in open('A-large.in'):
		if i==0:
			t=int(line)
			i=1
		else:
			st,m = line.split()
			inp.append((st,m))

def findcount(st,m):
	i=0
	n=len(st)
	count=0
	st=list(st)
	while i<=n-m:
		# print i,st,count
		if st[i]=='0':
			for j in range(i,i+m):
				st[j]=str(1-int(st[j]))
			count+=1
		i+=1
	for item in st:
		if item == '0':
			return "IMPOSSIBLE"
	return count

if __name__=='__main__':
	global res
	global inp
	inp=[]
	res=[]
	global t
	t=1
	readinput()
	for _ in range(t):
		st,m=inp[_]
		st=st.replace('+','1')
		st=st.replace('-','0')
		count=findcount(st,int(m))
		res.append(str(count))
	i=1
	with open('outputlarge.txt','a') as myfile:
		for item in res:
			myfile.write("Case #"+str(i)+": "+item+"\n")
			i+=1



