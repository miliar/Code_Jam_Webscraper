def letterorder(s):
	ret = ''
	for i in range(len(s)):
		if i==0 or s[i]<>s[i-1]:
			ret+=s[i]
	return ret
	
def lens(s):
	ret = []
	num = 1
	for i in range(1,len(s)):
		if s[i]<>s[i-1]:
			ret.append(num)
			num = 1
		else:
			num+=1
	return ret + [num]
	
print letterorder('aaabbbcdd')
print lens('aaabbbcdd')
	


f=open('temp.txt','rb')
g=open('submit.txt','wb')
for i in range(int(f.readline().strip())):
	g.write('Case #' + str(i+1) +': ')
	print i+1,':'
	elig = True
	n = int(f.readline().strip())
	ns=[]
	for j in range(n):
		ns.append(f.readline().strip())
	order = letterorder(ns[0])
	for j in ns[1:]:
		if letterorder(j) <> order:
			print letterorder(j),order
			elig = False
	if elig:
		nls = []
		for j in ns:
			nls.append(lens(j))
		tot = 0
		for j in range(len(order)):
			temp = [float(k[j]) for k in nls]
			avg = round(sum(temp)/len(nls))
			for k in temp:
				tot += abs(k-avg)
		g.write(str(int(tot)) + '\n')
	else:
		g.write('Fegla Won' + '\n')
			