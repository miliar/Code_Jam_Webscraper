
import sys

def gcd(a, b):
	while b:
		a%=b
		a,b = b,a
	return a

def lca(a, b):
	return a*b/gcd(a,b)
		
if __name__ == "__main__":
	
	fin = open(sys.argv[1], "r")
	data =fin.readlines();
	n_in = 0;
	total = int(data[n_in]);
	n_in += 1;
	for case in range(1, total + 1):
		n = int(data[n_in])
		n_in += 1;
		a = [int(item) for item in data[n_in].split()];
		n_in += 1;
		
		ans_x = 0;
		for i in range(1, n):
			ans_x += max(0, a[i - 1] - a[i])
			
		c = [max(a[i - 1] - a[i],0) for i in range(1, n)]
		b = [10 for i in range(1, n)]
		
		share = 1
		for i in range(n-1):
			share = gcd( b[i], c[i])
			c[i]/= share
			b[i]/= share
			
		share = 10
		for i in range(n-1):
			share = lca(share, b[i])
		ans_y = 0;
		vel = 0;
		for i in range(n-1):
			c[i] *= share/b[i]
			b[i] = share
			vel = max(10/b[i]*c[i],vel)
		for i in range(1,n):
			ans_y += min(vel, a[i - 1] )
			
		print "Case #"+str(case)+":", ans_x, ans_y