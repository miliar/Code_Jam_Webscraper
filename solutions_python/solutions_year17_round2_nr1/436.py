import sys 
sys.stdin = open("in.txt","r")
sys.stdout = open("out.txt","w")

for t in range(int(input())) : 
	d,n = map(int , input().split())
	ans = -1*float("inf")
	for i in range(n) : 
		s,v = map(int,input().split())
		ans = max(ans , abs(d-s) / v ) 
	print('Case #',t+1,': ',d/ans,sep = '')
	
