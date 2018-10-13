def is_tidy(n):
	prev=n%10
	n/=10
	while(n!=0):
		if(n%10>prev):
			return False
		prev=n%10
		n/=10
	return True

def digits(n):
	p=str(n)
	digit=[]
	for char in p:
		digit.append(int(char))
	return digit

def form(digits):
	n=0
	for digit in digits:
		n=n*10+digit
	return n

t=int(raw_input())

for i in xrange(t):
	n=int(raw_input())
	if is_tidy(n):
		print "Case #"+str(i+1)+": "+str(n)
		continue
	while(not is_tidy(n)):
		p=digits(n)
		l=len(p)
		for j in range(l-1):
			if p[j]>p[j+1]:
				p[j]-=1
				for k in range(j+1, l):
					p[k]=9
				break
		n=form(p)
	print "Case #"+str(i+1)+": "+str(n)
