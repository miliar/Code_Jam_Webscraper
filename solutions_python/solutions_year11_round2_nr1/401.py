def res(field):
	
	#print field
	
	games = arr(field)
	
	num = len(games)
	rnum = range(num)
	
	won = [sum(1.0 for c in t if c == True) for t in games]
	lost = [sum(1.0 for c in t if c == False) for t in games]
	nomatch = [sum(1.0 for c in t if c is None) for t in games]
	
	ngames = [lost[tn] + won[tn] for tn in rnum]
	
	def played(tn, opn):
		return games[tn][opn] is not None
	
	wps = [ won[tn] / ngames[tn] for tn in rnum ]
	#print "wps:", wps
	
	#print games
	#print "played", [ (a, b, played(a,b)) for a in rnum for b in rnum ]
	
	def wps_without(tn, wo):
		if played(tn, wo):
			return (wps[tn] * ngames[tn] - games[tn][wo]) / (ngames[tn]-1)
		else:
			return wps[tn]
	
	#print "wpsw", wps_without(1, 3)
	
	owps = [
		avg([
			wps_without(opn, tn)
			for opn in rnum
			if played(tn, opn)
		])
		for tn in rnum
	]
	#print "owps:", owps


	oowps = [
		avg([
			owps[opn]
			for opn in rnum
			if played(tn, opn)
		])
		for tn in rnum
	]
	#print "oowps:", oowps

	for tn in rnum:
		print rpi(wps[tn], owps[tn], oowps[tn])


def avg(l):
#	return sum(l) / len(l)
	s = 0.0
	c = 0
	for x in l:
		s += x
		c += 1
	return s / c


def arr(field):
	gamesit = range(len(field))
	
	pymap = {
		'1': True,
		'0': False,
		'.': None,
	}
	
	arr = [ [ pymap[g] for g in t ] for t in field ]
	#print arr
	return arr

def rpi(wp, owp, oowp):
	return 0.25 * wp + 0.50 * owp + 0.25 * oowp


if __name__ == "__main__":

	import sys

	filename = sys.argv[1]

	# Cut off case count
	caselines = open(filename).readlines()[1:]
	
	c = 0
	case = 1
	
	stripn = lambda s: s[:-1]
	
	while c < len(caselines):
		num = int(caselines[c])
		field = caselines[c+1:c+num+1]
		print "Case #%d:" % case
		res(map(stripn, field))
		c += num + 1
		case += 1

