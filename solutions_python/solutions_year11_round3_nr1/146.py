import sys,os

T = int(sys.stdin.readline())

class Impossible(Exception):pass

for case in range(T):
	rows = []
	R,C = [ int(x) for x in sys.stdin.readline().split() ]
	for r in range(R):
		rows.append( [ x for x in sys.stdin.readline().strip() ] )
	print "Case #%d:" % (case+1)
	try:
		x = []
		for i in range(R):
			r = rows[i]
			s = 0
			n_x = list()
			for j in range(C):
				if rows[i][j] == '.': 
					if s % 2: raise Impossible()
					s = 0
				if rows[i][j] == '#': 
					s+=1
					if not j in x:
						n_x.append(j)
						if s % 2 == 1: 
							rows[i][j] = '/'
						if s % 2 == 0:
							rows[i][j] = '\\'
					else:
						if s % 2 == 1: 
							rows[i][j] = '\\'
						if s % 2 == 0:
							rows[i][j] = '/'
				elif j in x: raise Impossible()
			x = n_x
			if s % 2: raise Impossible()
		if len(x): raise Impossible()
		for r in rows:
			print "".join(r)
	except Impossible:
		print "Impossible"
		