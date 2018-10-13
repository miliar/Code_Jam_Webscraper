def gcd(a, b):
	if(b==0):
		return a;
	else:
		return gcd(b, a%b);

def diff(a, b):
	if(a>b):
		return a-b;
	else:
		return b-a;

c=int(raw_input());
N=1010;
n=-1;

x=[0 for i in range(0, N)];

def find_T():
	g=diff(x[0], x[1]);
	for i in range(2, n):
		g=gcd(g, diff(x[i], x[i-1]));
	return g;

import sys;
write = sys.stdout.write;

for i in range(0, c):
	line=raw_input();
	item_List=line.split(' ');
	n=int(item_List[0]);
	for j in range(0, n):
		x[j]=int(item_List[j+1]);
	T=find_T();
	r=x[0]%T;
	r=T-r;
	if(r==T):
		r=0;
	write("Case #%d: %d\n" % (i+1, r));
