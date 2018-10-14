import bisect as bt
import sys
numbers = [0,1,4,9,121]
uniqnumbers = []
def search(x):
	return bt.bisect_right(uniqnumbers,x)

def run(case):

	a , b  = map(long,sys.stdin.readline().split()) 
#	print a,b;
#	print search(a-1),search(b);
	print 'Case #'+str(case)+': '+str(search(b)-search(a-1));	

def checkreverse(x):
	s = str(x);
	p = len(s)
	for i in range(p/2):
		if s[i] != s[-(i+1)]:
			return False;
	return True;

def init():
	Odd = ['0','1','2']	
	Even = ['11','00']	
	for i in range(3,50,2):
		for each in Odd:
			se = str(each)
			t = len(se);
			p = (i-t-2)/2;
			s = '1'+'0'*p+se+'0'*p+'1';
			x = long(s)
			xx = x**2;
			if (checkreverse(xx)):
				Odd.append(x)
				numbers.append(xx)
	for i in range(4,51,2):
		for each in Even:
			se = str(each)
			t = len(se);
			p = (i-t-2)/2;
			s = '1'+'0'*p+se+'0'*p+'1';
			x = long(s)
			xx = x**2;
			if (checkreverse(xx)):
				Even.append(x)
				numbers.append(xx)
	for i in range(3,51,2):
		p = (i-3)/2;
		s = '2'+'0'*p+'1'+'0'*p+'2';
		x = long(s)
		numbers.append(x**2)
	for i in range(2,51):
		s = '2'+'0'*(i-2)+'2'
		x = long(s)
		numbers.append(x**2)

	uniq = list(set(numbers))
	uniq.sort();
	return uniq;


uniqnumbers = init();
N = int(raw_input());
for i in range(1,N+1):
	run(i)


