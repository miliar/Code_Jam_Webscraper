import math

def check_fairsquare(n):
	root = int(math.sqrt(n))
	if( root*root != n):
		return False
	else:
		if(check_palindrome(n) == False):
			return False
		else:
			if(check_palindrome(root) == False):
				return False
			else:
				return True	
				

def check_palindrome(n):
	rev = 0;
	i = n;
	while(i > 0):
		rev = rev*10 + (i%10)
		i = int(i/10)
	if( n == rev):
		return True
	else:
		return False
	
if __name__=="__main__":
	t = input()
	ans = []
	for i in range(0,t):
		txt = raw_input()
		for j in range(0,len(txt)):
			if(ord(txt[j]) == 32):
				break
		a = int(txt[0:j])
		b = int(txt[j+1:])
		count = 0
		j = a
		while( j < b+1):
			root = int(math.sqrt(j))
			if( root*root != j):
				j = j+1
			elif( root*root == j) :
				break	
		
		while( j < b+1):
			if(check_palindrome(j)):
				if(check_palindrome(root)):
					count = count+1
			j = j+(2*root)+1
			root = root+1	  
		ans.append(count)
	for i in range(0,t):
		print 'Case',str('#')+str(i+1)+':',ans[i]	
		
