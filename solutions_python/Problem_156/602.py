import sys

with open(sys.argv[1],'rb') as f:
	T = int(f.readline())
	if 1<=T<=100:
		with open(sys.argv[2],'wb') as rf:
			for t in range(0, T):
				D = int(f.readline())
				Pline = f.readline().split(' ')
				P = []
				for i in range(0, D):
					Pi = int(Pline[i])
					P.append(Pi)
				time = max(P)
				for i in range(time, 1, -1):
					stime = i
					for Pi in P:
						add = (Pi-1)/i
						stime += add
					if stime<time:
						time = stime
				result = 'Case #'+str(t+1)+': '+str(time)
				rf.write(result+'\r\n')
