n = int(input())
def checkTidy(a):
	c = 10
	while a>0:
		r = a%10
		if(r>c):
			return False
		else:
			c = r
			a = int(a/10)
	return True
for i in range(n):
	inp = int(input())
	for j in range(inp,0,-1):
		if(checkTidy(j)):
			print("Case #",i+1,": ",j,sep="")
			break
