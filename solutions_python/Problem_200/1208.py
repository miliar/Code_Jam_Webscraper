def isTidy(n) :
	s = str(n)
	l = list(s)
	prev = 0
	for c in l :
		if prev > int(c) :
			return False
		prev = int(c)
	return True
	
#print(isTidy(12345))
#print(isTidy(54321))

def tidyUp(n):
	if isTidy(n) :
		return n
	return tidyUp(int(str(n)[:-1])-1) *10 + 9

t = int(input())
for i in range(0,t) :
	n = int(input())
	#print(n,tidyUp(n))
	print("Case #", i+1, ": ", tidyUp(n), sep="")
	