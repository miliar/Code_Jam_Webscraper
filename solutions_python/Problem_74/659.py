import sys
f=open(sys.argv[1])
f1=open("file.out", "w+")
N=int(f.readline())
for i in range(N):
	line=f.readline()
	spl=line.split(" ")
	b=int(spl[0])
	seq=spl[1:]
	co=1
	cb=1
	lto=0
	ltb=0
	t=0
	for j in range(b):
		if seq[2*j]=='O':
			l=abs(int(seq[2*j+1])-co)
			if lto+l<t:
				t+=1
			else:
				t=lto+l
				t+=1
			co=int(seq[2*j+1])
			lto=t
		elif seq[2*j]=='B':
			l=abs(int(seq[2*j+1])-cb)
			if ltb+l<t:
				t+=1
			else:
				t=ltb+l
				t+=1
			cb=int(seq[2*j+1])
			ltb=t
	f1.write("Case #" + str(i+1) + ": " + str(t)+"\n")
