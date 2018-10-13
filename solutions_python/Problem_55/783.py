import sys

f=open("C-small-attempt0.in","r")
T=int(f.readline())
i=0
while i<T:
	values=f.readline()
	RkN=values.split()
	R=int(RkN[0])
	k=int(RkN[1])
	N=int(RkN[2])	

	q=f.readline()
	q_tmp=q.split()
	queue=[]
	for element in q_tmp:
		queue.insert(0,int(element))
	total_cost=0

	r=0
	while r<R:
		people_in_ride=0
		groups=0
		while people_in_ride<k and groups<N:
			g=queue.pop()
			if g+people_in_ride>k:
				queue.append(g)
				break
			else:
				people_in_ride=people_in_ride+g
				queue.insert(0,g)
				groups=groups+1
		total_cost=people_in_ride+total_cost
		r=r+1
	sys.stdout.write("Case #")
	sys.stdout.write(str(i+1))
	sys.stdout.write(": ")
	sys.stdout.write(str(total_cost))
	sys.stdout.write("\n")
	i=i+1
