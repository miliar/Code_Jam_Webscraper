f = open('input.txt')
cases = int(f.readline().rstrip('\n'))

for case in range (1,cases+1):
	n,t = [int(x) for x in f.readline().split(" ")]
	if(t==1) : print("Case #"+str(case)+": "+str(int(n/2))+" "+str(int(n/2)-(n+1)%2))
	else : 
		i=1
		pow2=2
		while(pow2 <= t):
			i=i+1
			pow2=pow2*2

		if(pow2>t) :
			i=i-1
			pow2=pow2/2

		scat = str('%f' % ((n+1-t)/pow2))

		cat = int(scat.split(".")[0])
		if(len(scat.split("."))>1 and int(scat.split(".")[1])!=0) : cat = cat+1

		print("Case #"+str(case)+": "+str(int(cat/2))+" "+str(int(cat/2)-(cat+1)%2))
