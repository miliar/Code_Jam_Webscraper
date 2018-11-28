f = open('input.in')
out = open('output','w')
lines = f.readlines()
T = int(lines[0])
for i in range(T):
	C,F,X = lines[i+1].rstrip('\n').split(' ')
	
	sec = 0
	oend = 0
	x=0
	while True :
		usine = float(C)/(2+(float(x)*float(F)))
		endnow = float(X)/(2+(float(x)*float(F)))
		endlater= float(X)/(2+(float(x+1)*float(F)))
		if (usine+endlater > endnow):
			out.write("Case #%d: %.7f \n"%(i+1, sec+endnow))
			break;
		sec = sec+usine
		x = x+1
f.close()
out.close()