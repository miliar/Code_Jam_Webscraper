def check(str):
	for x in str:
		if x=='-':
			return False
	return True

def swap(s,i,k):
	res = ""
	for x in range(0,i):
		res = res + s[x]
	for x in range(i,i+k):
		if s[x] =='-':
			res=res+'+'
		else:
			res=res+'-'
	for x in range(i+k,len(s)):
		res = res + s[x]
	return res
				

def solve():
	r = open('input.in','r')
	f = open('output.out','w')
		

	t = int(r.readline())
	for j in range(1,t+1):
		
		s,k = str(r.readline()).split()
		k = int(k)
		data = {}
		data[s] = 1
		ans = 0
		while not check(s):
			for i in range(0,len(s)):
				if s[i]=='-' and i+k<=len(s):
					s = swap(s,i,k)
					ans = ans + 1				
			if s in data:
				ans='IMPOSSIBLE'
				break
			else:
				data[s] = 1	
				
		f.write('Case #'+str(j)+': '+str(ans)+'\n')
	r.close()
	f.close()

solve()














