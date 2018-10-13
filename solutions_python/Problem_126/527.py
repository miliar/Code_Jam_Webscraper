import math

def valid(ss,a):
	for i in range(len(ss)-a+1):
		x = ss[i:i+a]
		
		if len(x) == a:
			p = True
			for c in x:
				if c in ['a','e','i','o','u']:
					p = False
			
			if p:
				return True
	return False
		
def main():
	test = 1
	
	IN = open('A-small-attempt0.in','r+')
	OUT = open('ANSWER.out', 'w+')
	
	T = int(IN.readline())
	
	for t in range(T):
		_line = IN.readline().split(' ')
		
		s = _line[0]
		a = int(_line[1])
		answer = 0
		
		for i in range(len(s)-a+1):
			for j in range(i+a,len(s)+1):
				if valid(s[i:j],a):
					answer = answer + 1 
		
		
		
		print "Case #%d: %d" % (t+1,answer)
		OUT.write("Case #%d: %d\n" % (t+1,answer))
			
		test += 1

	IN.close()
	OUT.close()
	
if __name__ == '__main__':
	main()

