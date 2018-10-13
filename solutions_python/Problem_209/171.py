import math

fin = open("D:/input.in", "r")
fout = open("D:/output.txt", "w")
lines = fin.readlines()
ll = 0
cases = int(lines[ll])
ll+=1
for x in range(0,cases):
	(n, k) = map(int,lines[ll].split(" "))
	ll+=1
	pank = []
	for y in range(0, n):
		(r, h) = map(int,lines[ll].split(" "))
		ll+=1
		pank.append((-2*r*h, -r*r))
	pank.sort()	
	sum = 0;
	max = 0;
	for i in range(0, k-1):
		(a,b) = pank[i]
		(a,b) = (-a, -b)
		sum+=a
		if b>max:
			max = b
	maxx = 0;
	for i in range(k-1, n):
		(a,b) = pank[i]
		(a,b) = (-a, -b)
		sum = sum+a;
		if b > max:
			ans = sum+b;
		else:
			ans = sum+max;
		if ans>maxx:
			maxx = ans
		sum = sum-a;
	fout.write("Case #"+str(x+1)+": "+str(maxx*math.pi)+"\n")
	
fout.close()
