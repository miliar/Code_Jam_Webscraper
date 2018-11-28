#!/usr/bin/python

import sys

def main ():
	args = sys.argv[1:]
	
	f = open(args[0])
	ncases = int(f.readline())
	
	for i in xrange(0, ncases):
		order = f.readline().rsplit()
		nmovs = int(order.pop(0))
		
		Op = 1
		Bp = 1
		Om = []
		Bm = []
		
		for j in xrange(0, nmovs):
			R = order.pop(0)
			mov = int(order.pop(0))
			
			if R == 'O':
				if mov > Op:
					Om += ['r']*(mov-Op)
				elif mov < Op:
					Om += ['l']*(Op-mov)
				Op = mov
				Om.append('p')
				
				lB = len(Bm)
				if len(Om) <= lB:
					Om += ['w']*(lB-len(Om)+1)
			elif R == 'B':
				if mov > Bp:
					Bm += ['r']*(mov-Bp)
				elif mov < Bp:
					Bm += ['l']*(Bp-mov)
				Bp = mov
				Bm.append('p')
				
				lO = len(Om)
				if len(Bm) <= lO:
					Bm += ['w']*(lO-len(Bm)+1)
		
		print "Case #"+str(i+1)+":", max(len(Om),len(Bm))

if __name__ == "__main__":
	main ()
