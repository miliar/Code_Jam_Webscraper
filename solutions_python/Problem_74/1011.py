import sys

K=int(sys.stdin.readline())
for kk in range(K):
	line=sys.stdin.readline().split()
	N=int(line[0])
	r=[1,1]
	w=[0,0]
	res=0
	for i in range(N):
		side=0 if line[2*i+1]=='O' else 1
		ind=int(line[2*i+2])
		dist=max( abs(r[side] - ind)-w[side], 0)
		time_to_switch=dist+1
		res+=time_to_switch
		r[side]=ind
		w[side]=0
		w[1-side]+=time_to_switch
	print "Case #%d: %d"%(kk+1,res)
