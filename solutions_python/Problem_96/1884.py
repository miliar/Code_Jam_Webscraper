def main(line):
	n = int(line.split(' ')[0])
	s = int(line.split(' ')[1])
	p = int(line.split(' ')[2])
	t = list()
	flaga=0
	flagb=0
	flagc =0
	l = [[(0,0,-1),(0,0,-1)],[(0,0,-1),(0,0,-1)],[(0,0,-1),(0,0,-1)],[(0,0,-1),(0,0,-1)],[(0,0,-1),(0,0,-1)],[(0,0,-1),(0,0,-1)]]
	for x in xrange(n+3):
	  if x >= 3 :
	    t = t + [int(line.split(' ')[x])]
	for y in xrange(n) :
	  if t[y] == 0 :
	    l[y][0] = [(0,0,0)]
	    l[y][1] = [(0,0,-1)]
	  elif t[y] == 1 :
	    l[y][0] = [(0,0,1)]
	    l[y][1] = [(0,0,-1)]
	  elif t[y] == 3 :
	    l[y][0] = [(0,0,-1)]
	    l[y][1] = [(0,1,2)]
	  elif t[y] == 2 :
	    l[y][0] = [(0,1,1)]
	    l[y][1] = [(0,0,2)]
	  elif t[y] == 4 :
	    l[y][0] = [(2,1,1)]
	    l[y][1] = [(0,2,2)]
	  elif t[y] == 5 :
	    l[y][0] = [(2,1,2)]
	    l[y][1] = [(3,1,1)]
	  elif t[y] == 6 :
	    l[y][0] = [(2,2,2)]
	    l[y][1] = [(3,1,2)]
	  elif t[y] == 7 :
	    l[y][0] = [(3,2,2)]
	    l[y][1] = [(3,3,1)]
	  elif t[y] == 8 :
	    l[y][0] = [(3,3,2)]
	    l[y][1] = [(4,2,2)]
	  elif t[y] == 9 :
	    l[y][0] = [(3,3,3)]
	    l[y][1] = [(4,3,2)]
	  elif t[y] == 10 :
	    l[y][0] = [(4,4,2)]
	    l[y][1] = [(3,3,4)]
	  elif t[y] == 11 :
	    l[y][0] = [(4,4,3)]
	    l[y][1] = [(3,3,5)]
	  elif t[y] == 12 :
	    l[y][0] = [(4,4,4)]
	    l[y][1] = [(5,4,3)]
	  elif t[y] == 13 :
	    l[y][0] = [(5,4,4)]
	    l[y][1] = [(5,5,3)]
	  elif t[y] == 14 :
	    l[y][0] = [(5,4,5)]
	    l[y][1] = [(6,4,4)]
	  elif t[y] == 15 :
	    l[y][0] = [(5,5,5)]
	    l[y][1] = [(6,5,4)]
	  elif t[y] == 16 :
	    l[y][0] = [(6,5,5)]
	    l[y][1] = [(6,6,4)]
	  elif t[y] == 17 :
	    l[y][0] = [(6,6,5)]
	    l[y][1] = [(7,5,5)]
	  elif t[y] == 18 :
	    l[y][0] = [(6,6,6)]
	    l[y][1] = [(7,6,5)]
	  elif t[y] == 19 :
	    l[y][0] = [(7,6,6)]
	    l[y][1] = [(7,7,5)]
	  elif t[y] == 20 :
	    l[y][0] = [(7,7,6)]
	    l[y][1] = [(8,6,6)]
	  elif t[y] == 21 :
	    l[y][0] = [(7,7,7)]
	    l[y][1] = [(8,7,6)]
	  elif t[y] == 22 :
	    l[y][0] = [(8,7,7)]
	    l[y][1] = [(8,8,6)]
	  elif t[y] == 23 :
	    l[y][0] = [(8,8,7)]
	    l[y][1] = [(9,7,7)]
	  elif t[y] == 24 :
	    l[y][0] = [(8,8,8)]
	    l[y][1] = [(9,8,7)]
	  elif t[y] == 25 :
	    l[y][0] = [(9,8,8)]
	    l[y][1] = [(9,9,7)]
	  elif t[y] == 26 :
	    l[y][0] = [(9,9,8)]
	    l[y][1] = [(10,8,8)]
	  elif t[y] == 27 :
	    l[y][0] = [(9,9,9)]
	    l[y][1] = [(10,9,8)]
	  elif t[y] == 28 :
	    l[y][0] = [(10,9,9)]
	    l[y][1] = [(10,10,8)]
	  elif t[y] == 29 :
	    l[y][0] = [(10,10,9)]
	    l[y][1] = [(10,10,9)]
	  elif t[y] == 30 :
	    l[y][0] = [(10,10,10)]
	    l[y][1] = [(10,10,10)]
	for i in xrange(n):
	  flagc = 0
	  for j in xrange(2) :
	      if flagc == 9 :
		break
	      else :
		for k in xrange(3) :
		    if s >=flagb :
			if l[i][j][0][k] >= p :
			    if j== 1 :
			      if s== flagb :
				break
			      elif j==1 :
				flagb = flagb +1
			    flaga = flaga +1
			    flagc=9
			    break
			    
		
	return flaga


if __name__ == '__main__':
	import sys
	N = int(sys.stdin.readline())
	for i in xrange(N):
		res = main(sys.stdin.readline().strip())
		print "Case #%d: %s" % (i + 1, res)	
