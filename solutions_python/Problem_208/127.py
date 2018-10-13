#!/usr/bin/python
import sys

import heapq

def find_fastest(F,T,H,D):
	#data [time so far, current city, current horse remaining duration, current horse speed, used horses]
	start_data=[0,F,H[F][0],H[F][1],[]]
	hp = [start_data]
	
	#best time when horse at city N exchanged
	h_set={F:0}
	
	found=False
	best_time=0

	while hp:
		cur_data=heapq.heappop(hp)
#		print(cur_data)
		time,city,h_dur,h_spd,h_out=cur_data

		if found & (time>=best_time):
			return best_time

		if city==T:
			found=True
			best_time=time

		else:
			for i,dist in enumerate(D[city]):
				if dist==-1:
					continue

				if dist<= h_dur:
					if (h_dur>=H[city][0]) | (h_spd>=H[city][1]):
						next_data=[time+dist/h_spd,i,h_dur-dist,h_spd,h_out[:]]
						heapq.heappush(hp,next_data)

				if not(city in h_out):
					if dist<=H[city][0]:
						h_out_n=h_out[:]
						h_out_n.append(city)
						next_data=[time+dist/H[city][1],i,H[city][0]-dist,H[city][1],h_out_n]
						heapq.heappush(hp,next_data)
	return -1


fi = open(sys.argv[1]) if len(sys.argv) > 1 else sys.stdin
fo = open(".".join(sys.argv[1].split('.')[:-1])+".out","w") if len(sys.argv) > 1 else sys.stdout

TC=int(fi.readline())
for i in range(1,TC+1):
	ln=fi.readline().split()
	N=int(ln[0])
	Q=int(ln[1])
	H=[]
	D=[]
	RQ=[]
	TQ=[]
	for n in range(N):
		ln=fi.readline().split()
		H.append([int(ln[0]),int(ln[1])])
	for n in range(N):
		ln=fi.readline().split()
		Di=[]
		for d in ln:
			Di.append(float(d))
		D.append(Di)

	for q in range(Q):
		ln=fi.readline().split()
		RQ.append([int(ln[0])-1,int(ln[1])-1])
	TQ=[]
	for q in range(Q):
		TQ.append(find_fastest(RQ[q][0],RQ[q][1],H[:],D))
					
	print("Case #{}: {}".format(i," ".join(map(str,TQ))),file=fo)

