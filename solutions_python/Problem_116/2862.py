import sys
def readinput(filen):
	f = open(filen,'r').readlines()[1:]
	out = []
	game=[]
	for line in f:
		if line != "\n":
			game.append(line.strip())
		else:
			out.append(game)
			game= []
	out.append(game)
	game= []
	#print out
	return out[:-1]

input = readinput(sys.argv[1])
won = {}
def check_win(C,g,x,y,xaddentum,yaddentum):
	#import pdb;pdb.set_trace()
	try:
		if g[x][y] == g[x + xaddentum][y+yaddentum] == g[x+(xaddentum*2)] [y+(yaddentum*2)] != '.':
			if g[x+xaddentum*3][y+yaddentum*3] == g[x][y] or g[x+xaddentum*3][y+yaddentum*3] == 'T':
				#print C,g[x][y], "won",x,y
				won[C]="%s won"%(g[x][y])
				return 1
				#import pdb;pdb.set_trace()
	except:
		#print g
		#import pdb;pdb.set_trace()
		pass
def printwon():
	for k in won.keys():
		#print k , won[k]	
		print "Case #%s: %s"%(k,won[k])
def check_rc(C,g):
	#print g
	#if g == ['OXXX', 'XXXT', 'OOXO', 'OOOX']:import pdb;pdb.set_trace()
	#import pdb;pdb.set_trace()
	try:
		for x in 1,2:
			if g[x][0] == g[x][1] == g[x][2] != '.':
				if g[x][0] == g[x][3] or g[x][3] == 'T':
					won[C] = "%s won"%(g[x][0])
					return 1


		for y in 1,2:
			if g[0][y] == g[1][y] == g[2][y] != '.':
				if g[0][y] == g[3][y] or g[3][y] == 'T':
					won[C] = "%s won"%(g[0][y])
					return 1
	except:
		pass

def check_draw(C,g):
	#if g == ['XTXO', 'O...', 'XXOO', 'O.XX']: import pdb;pdb.set_trace()
 	for r in g:
		if r.find('.')>-1:return 
		if (not won.has_key(C)) and (r.find('.')<0):
			pass
	if not won.has_key(C):
		won[C] = "Draw"
		return 1
	

for game in input:
	C = input.index(game)
	status = 0
	vdict={
		(0,0):[[0,1],[1,0],[1,1]],
		(3,0):[[0,1],[-1,0],[-1,1]],
		(0,3):[[0,-1],[-1,0],[1,-1]],
		(3,3):[[-1,0],[0,-1],[-1,-1]]
		}
	for key in vdict.keys():
		for v in vdict[key]:
			status = check_win(C+1,game,key[0],key[1],v[0],v[1])
			if status == 1:
				break
			#print status
			#check_win(1,game,0,0,0,1)
	#if game == ['XOXX', 'OOXO', 'OOOX', 'XXXT']: import pdb;pdb.set_trace()
	if status == 1:continue
	if not status :status = check_rc(C+1,game)
	if not status: status = check_draw(C+1,game)
	#if game == ['XOX.', 'OX..', '....', '....']:import pdb;pdb.set_trace()
	#print status
	if not status and not won.has_key(C+1):
		won[C+1] = "Game has not completed"
	

printwon()
			
		 	
	
