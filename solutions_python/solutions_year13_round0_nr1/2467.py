import sys, os

sample = """6
XXXT
....
OO..
....

XOXT
XXOO
OXOX
XXOO

XOX.
OX..
....
....

OOXX
OXXX
OX.T
O..O

XXXO
..O.
.O..
T...

OXXX
XO..
..O.
...O"""



def funkity(l):
	t = int(l.pop(0))
	result = ""
	for game in xrange(t):
		gameresult = False
		e_s = False #assume game complete
		g = l.pop(0) + l.pop(0) + l.pop(0) + l.pop(0)
		if len(l) > 0: l.pop(0)
		if '.' in g:
			if g.count('.') > 10:
				result += "Case #%i: Game has not completed\n" % (game+1)
				continue
			else:
				e_s = True
		for x in xrange(4): #(tc = 5*tc)
			m = [g[x*4:x*4+4], g[x:x+13:4]]
			if x == 0: m += g[3:13:3], g[0:16:5]
			for tc in m:
				if '.' in tc or ('X' in tc and 'O' in tc) or tc.count('T') > 1:
					continue
				else:
					for player in ['X', 'O']:
						if tc.count(player) + tc.count('T') == 4:
							result += "Case #%i: %s won\n" % (game+1, player)	
							gameresult = True
							break
				if gameresult:
					break
			if gameresult:
				break
		if not gameresult:
			if e_s:
				result += "Case #%i: Game has not completed\n" % (game+1)
			else:
				result += "Case #%i: Draw\n" % (game+1)
	return result



if __name__=='__main__':
    with open('output.txt', 'w') as outputfile:
        if len(sys.argv) < 2:
        	print funkity(sample.split('\n'))
            #outputfile.write(funkity(sample.split('\n')))
        else:
            with open(sys.argv[1], 'r') as input:
                outputfile.write(funkity([j.rstrip() for j in input.readlines()]))



