f = file("input",'r')
o = file("output",'w')
def calc_recycle(p):
	for i in range(1,len(str(p))):
		q = p / (10 ** i)
		r = p % (10 ** i)
		num = (r*(10 ** len(str(q))) + q)
		if  num <= int(b[1]) and num > p:
			if not (p,num) in a:
				a.append((p,num))


lines = f.readlines()
for c in range(1,int(lines[0])+1):
		o.write("Case #%d"%c+": ")
		a=[]
		b = lines[c].split()
		for i in range(int(b[0]),int(b[1])+1):
			if i%10 != i:
				calc_recycle(i)
		length = len(a)		
		o.write('%d'%length+'\n')	

f.close()
o.close()
