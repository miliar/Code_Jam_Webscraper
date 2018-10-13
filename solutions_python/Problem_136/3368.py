fileR = 'B-small-attempt0.in'
f = open(fileR,'r')
l = f.readlines()

for i in range(0,len(l)):
	l[i] = l[i].strip()
	l[i] = l[i].split(' ')

test = int(l[0][0])
l = l[1:]

f = open('B-small-attempt0.out','w')

count = 1

while count<=test:
	C = float(l[0][0])
	F = float(l[0][1])
	X = float(l[0][2])
#	print(C,F,X)
	l = l[1:]
	rate = 2.0
	time = 0.0
	while 1:
		t1 = round(X/rate,7)
		t2 = round((C/rate)+(X/(rate+F)),7)
#		print(t1,t2)
		if t1<=t2:
			time = round(time + t1,7)
			break; 
		time = round(time + (C/rate),7)
 		rate = rate + F
	f.write("Case #"+str(count)+": "+str(time)+"\n")
	count = count+1
f.close()

#end of program
