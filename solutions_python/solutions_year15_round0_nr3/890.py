def quat(a, b):
	s = '-' if (a[0]=='-') != (b[0]=='-') else ''
	if a[0]=='-': a=a[1:]
	if b[0]=='-': b=b[1:]
	if a=="1": return s+b
	if b=="1": return s+a
	if a==b or (ord(b)-ord(a)+3)%3==2: s = '-' if s=='' else ''
	if a==b: return s+'1'
	elif ord(b)<ord(a): a,b=b,a
	return s+ {'i':{'j':'k','k':'j'},'j':{'k':'i'}}[a][b]


T = int(raw_input())

for t in range(1,1+T):
	L, X = map(int,raw_input().split(' '))
	s = raw_input()*X
	m = []
	for i in range(len(s)):
		m.append(s[i] if i==0 else quat(m[-1],s[i]))
	ends = []
	for i in range(len(s)-1, -1, -1):
		ends.append(s[i] if i==len(s)-1 else quat(s[i],ends[-1]))
	ends.reverse()
	w = "NO"
	for i in range(len(s)):
		if w=="YES": break
		if m[i]!='i': continue
		for k in range(i+1,len(s)):
			if ends[k]!='k': continue
			if quat(quat(m[i],m[i]), quat(m[i],m[k-1]))=='j':
				w = "YES"
#				print(reduce(quat, s[:i+1]))
#				print(reduce(quat, s[i+1:k]))
#				print(reduce(quat, s[k:]))
				break
	print("Case #%s: %s" % (t, w) )
