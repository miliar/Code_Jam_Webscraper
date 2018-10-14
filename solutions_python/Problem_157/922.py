table = [["1","i","j","k"],["i","-1","k","-j"],["j","-k","-1","i"],["l","j","-i","-1"]]
def multiply(i,j):
	
	if(len(i)>1 and len(j) > 1):
		negative = False
	elif len(i)>1 or len(j) > 1:
		negative = True
	else:
		negative = False
	i = i.strip('-')
	j = j.strip('-')
	prod = table[table[0].index(i)][table[0].index(j)]
	if(len(prod)>1 and negative==True):
		prod=prod[1]
	elif(len(prod)==1 and negative==True):
		prod='-'+prod[0]
	return prod

def m(s):
	p = s[0]
	t = {}
	f = True
	prod = '1'
	i=0
	for c in s:
		
		prod = multiply(prod,c)
		if p != c:
			f = False
		i+=1
	if(f == True and i>1):
		prod = 0
	return prod

def sub(s):
	if(m(s) != '-1'):
		return 'NO'
	for p1 in range(1,len(s)-1):
		s1 = s[0:p1]
		i = m(s1)
		if(i == 'i'):
			for p2 in range(p1+1,len(s)):
				s2 = s[p1:p2]
				j = m(s2)
				if(j == 'j'):
					s3 = s[p2:]
					k = m(s3)
					if(k == 'k'):
						return 'YES'
	return 'NO'
				
	
				
if __name__ == "__main__":
	testcases = input()
     
	for caseNr in xrange(1, testcases+1):
		print("Case #%i:" % caseNr),
		i = int(raw_input().split(' ')[1])
		s = raw_input()
		print(sub(s*i))