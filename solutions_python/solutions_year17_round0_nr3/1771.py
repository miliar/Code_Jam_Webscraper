import sys
sys.stdin = open("in.txt","r")
sys.stdout =  open("out.txt","w")
from math import floor,ceil,log
def div(n) :
	if n&1 == 1: return [n>>1,n>>1]
	else: return [n>>1,(n>>1)-1]

def bar(n,k) :
	h = floor(log(k,2))
	if k == 1 :
		return div(n)
	i = 1
	t1,t2 = div(n)
	cnt = [1,1]
	while i < h :
		d = [0,0]
		a,b = div(t1)
		c,d = div(t2)
		s = set([a,b,c,d])
		if len(s) == 1 :
			cnt[0] = cnt[0]*2 ; cnt[1] = cnt[1]*2
			t1 = t2 = list(s)[0]
		else:
			nc = [0,0]
			x = t1>>1 ; y = (t1>>1) - 1
			if a == x : nc[0] += cnt[0]
			elif a == y : nc[1] += cnt[0]
			if b == x : nc[0] += cnt[0]
			elif b == y : nc[1] += cnt[0]
			if c == x : nc[0] += cnt[1]
			elif c == y : nc[1] += cnt[1]
			if d == x : nc[0] += cnt[1]
			elif d == y : nc[1] += cnt[1]
			cnt= nc
			t1 = x
			t2 = y
		i += 1
	rem = k - pow(2,h) + 1
	if rem > cnt[0] : return div(t2)
	else : return div(t1)

for t in range(int(input())) : 
	n,k = map(int,input().split())
	ans = sorted(bar(n,k))[::-1]
	print("Case #",t+1,": ",ans[0],' ',ans[1],sep = '')