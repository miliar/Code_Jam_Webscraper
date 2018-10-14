import sys
f=open(sys.argv[1])
f1=open("candy.out", "w+")
N=int(f.readline())
for i in range(N):
	c=int(f.readline())
	line=f.readline()
	spl=line.split(" ")
	maxrsum=-1
	for j in range(c):
		spl[j]=int(spl[j])
	for j in range(1,2**c-1):
		order=bin(j)[2:].rjust(c,'0')
		sum1=0
		sum2=0
		realsum=0
		for k in range(c):
			if order[k]=='0':
				sum1 = sum1 ^ spl[k]
			else:
				sum2 = sum2 ^ spl[k]
				realsum = realsum + spl[k]
		if sum1==sum2:
			if realsum>maxrsum:
				maxrsum=realsum
	if maxrsum==-1:
		f1.write("Case #" + str(i+1) + ": NO\n")
	else:
		f1.write("Case #" + str(i+1) + ": " + str(maxrsum) + "\n")
