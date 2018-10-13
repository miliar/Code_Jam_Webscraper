#inc is the number of factories you buy
#Then divide X by final speed = C + inc*F
def cookie(C,F,X,inc):
	t = 0
	for i in range(inc):
		t += C/(2+i*F)
	t += X/(2+inc*F)
	return t

f = open('B-small-attempt0.in','r')
T = int(f.readline().strip())
w = open('outputCookieClicker.txt', 'w')
for i in range(T):
	stri = f.readline().split()
	C = float(stri[0])
	F = float(stri[1])
	X = float(stri[2])
	inc = 0#Try all costs until it starts going up
	cost = cookie(C,F,X,inc)
	inc += 1
	nextCost = cookie(C,F,X,inc)
	while (nextCost < cost):
		inc += 1
		cost = nextCost
		nextCost = cookie(C,F,X,inc)
	w.write("Case #" + str(i+1) +": " + str(cost)+"\n")
	
