f = open('text.in', 'r')
f1 = open('text.out','w')
fl=0

def bad(s):
	if 1==len(s):
		return 0
	if s[0]>s[1]:
		return 1
	return bad(s[1:])

def czx(s):
	line=s
	res=line
	for i in range(len(line)-1):
		if line[i]>line[i+1]:
			w=str(int(line[i])-1)
			res=czx(line[0:i]+w+'9'*(len(line)-1-i))	
			break
	return res

for line in f:
	if fl<1:
		fl=1
		continue
	fl=fl+1
	line=line[0:-1]
	res=czx(line)
	q=int(res)
	f1.write("Case #"+str(fl-1)+": "+str(int(res))+'\n')
f.close()
f1.close()
