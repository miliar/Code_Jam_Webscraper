import sys 
sys.stdin = open("in.txt","r")
sys.stdout = open("out.txt","w")
def foo(n) :
	if bar(n) : return n 
	n = list(str(n))
	t = []
	prev = '9'
	for i in range(len(n)-1 , -1 , -1 ) :
		if n[i] > prev :
			t = ['9'] * len(t)
			prev = str(int(n[i])-1)
			t.append(prev)
		else :
			t.append(n[i])
			prev = n[i]
	return int(''.join(t[::-1]))

def bar(n) :
	prev = n%10 ; n //= 10
	flag = True
	while n > 0 and flag:
		m = n%10
		n //= 10
		if m > prev :
			flag = False
		prev = m
	return flag
	
for t in range(int(input())) :
	n = int(input())
	print('Case #',t+1,': ',foo(n),sep = '')