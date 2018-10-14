
from fractions import gcd;

def ggcd(n, lst):
	j = 0;
	while j < n and lst[j] == 0:
		j = j + 1;
	if j >= n:
		return 0;
	g = lst[j];
	while j < n:
		g = gcd(g, lst[j]);
		j = j + 1;
	return g;

def doit(i, lst):
	n = int(lst[0]);
	j = 1;
	nlst = [];
	while j <= n:
		nlst.append(int(lst[j]));
		j = j + 1;
	nlst.sort();
	
	#print(nlst);
	
	factors = [];
	j = 0;
	while j < n-1:
		factors.append(nlst[j+1]-nlst[j]);
		j = j + 1;
	
	#print(factors);
		
	g = ggcd(n-1, factors);
	
	if g == 0:
		return 0;
	
	gap = g - nlst[0]%g;
	
	#print("gcd");
	#print(g);
	#print(gap);
	
	c = 0;
	while 1:
		ok = 1;
		j = 0;
		while j < n:
			if nlst[j]%g != 0:
				ok = 0;
				k = 0;
				while k < n:
					nlst[k] = nlst[k] + gap;
					k = k + 1;
				#print(nlst);
				c = c + gap;
				if gap != g:
					gap = g;
				break;
			j = j + 1;
		if ok == 1:
			return c;
	

def main():
	c = input();
	i = 1;
	while i <= int(c):
		st = input();
		lst = st.split();
		print('Case #' + str(i) + ': ' + str(doit(i, lst)));
		i = i + 1;
	
main();
