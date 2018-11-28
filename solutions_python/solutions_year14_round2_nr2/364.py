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
	tot = 0
	g.write('Case #' + str(i+1) + ': ')
	[a,b,k] = map(int,f.readline().strip().split())
	for x in range(a):
		for y in range(b):
			if x & y < k:
				tot +=1
	g.write(str(tot) + '\n')

			