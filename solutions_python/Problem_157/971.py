import math
import sys
 
def prod(x, y):
	z = ""
	if ("-" in x and "-" in y) or ("-" not in x and "-" not in y):
		m = 1
	else:
		m = -1
	
	if "i" in x:
		if "j" in y:
			z = z+"k"
		elif "k" in y:
			z = z+"j"
			m *= -1
		elif "i" in y:
			z = z+"1"
			m *= -1
		else:
			z = z+"i"
			
	elif "j" in x:
		if "i" in y:
			z = z+"k"
			m *= -1
		elif "k" in y:
			z = z+"i"
		elif "j" in y:
			z = z+"1"
			m *= -1
		else:
			z = z+"j"
	
	elif "k" in x:
		if "i" in y:
			z = z+"j"
		elif "j" in y:
			z = z+"i"
			m *= -1
		elif "k" in y:
			z = z+"1"
			m *= -1
		else:
			z = z+"k"
	
	elif "1" in x:
		if "i" in y:
			z = z+"i"
		elif "j" in y:
			z = z+"j"
		elif "k" in y:
			z = z+"k"
		else:
			z = z+"1"
			
	if m == -1:
		z = "-"+z;
			
	return z;

def get_next_k(s):
	n = len(s)
	a = "1"
	r = range(n)
	r.reverse()
	next_k = -1
	for k in r:
		a = prod(s[k], a)
		if a == "k":
			next_k = k
			break;
	
	return next_k;

def get_next_i(s):
	n = len(s)
	a = "1"
	next_i = -1
	for i in range(n):
		a = prod(a, s[i])
		if a == "i":
			next_i = i
			break;
	return next_i;
	
def find_j(s,m,n):
	a = "1"
	for i in range(m,n):
		a = prod(a, s[i])
	
	if a == "j":
		return 1;
	else:
		return 0;

def foo(s):
	n = len(s)
	if n <= 2:
		return 0;
	finish = 0
	list_i = []
	list_k = []
	
	next_i = get_next_i(s)
	next_k = get_next_k(s)
	
	is_j = 0
	if next_i != -1 and next_i < next_k:
		is_j = find_j(s, next_i+1, next_k)	
		
	return is_j
		
def main():
	f = open(sys.argv[1], 'r')
	l = f.readlines()	
	n = int(l[0])
	k = 0
	i = 1
	while (k < n):
		t = int((l[i].split())[1])
		s = l[i+1]
		s = s.strip()
		s = s*t
		r = foo(s)
		if r == 1:
			print "Case #" + str(k+1) + ": YES"
		else:
			print "Case #" + str(k+1) + ": NO"
		k += 1
		i += 2
		
if __name__ == '__main__':
	main()