import psyco
import sys

psyco.full()

test_input = r'''7
30.0 1.0 2.0
30.0 2.0 100.0
30.50000 3.14159 1999.19990
500.0 4.0 2000.0
9991.58989 1.23748 99985.40872
6202.00000 53.00000 6575.00000
9995.72236 1.48570 99995.06855'''.split('\n')

DEBUG = False

def debug(s, s2=None):
	if not DEBUG:
		return
	if s2 is not None:
		print s, s2
	else:
		print s

def readline():
	
	if DEBUG:
		return test_input.pop(0)
	return raw_input()

def case(casenum):
	
	# c = farm cost
	# f = farm extra cookies per second
	# x = win amount (unspent)
	farmcost, farmbonus, winamount = map(float, readline().split(' '))
	
	# cookies per second
	cps = 2
	cookies = 0
	seconds = 0
	
	wintimes = set()
	
	# win time if nothing is bought
	wintime = winamount / cps
	wintimes.add(wintime)
	m = wintime
	
	while seconds <= m:
		# buy a farm
		sec_buy_farm = (farmcost - cookies) / cps
		cookies += sec_buy_farm * cps
		seconds += sec_buy_farm
		cookies -= farmcost
		cps += farmbonus
		wintime = seconds + (winamount / cps)
		if wintime < m:
			m = wintime
			wintimes.add(wintime)
		# debug([wintime, seconds, cookies])
	
	# lowest possible win time is the output
	output = min(wintimes)
	print "Case #%d: %.7f" % (casenum, output)
	sys.stderr.write(str(casenum) + '\n')
	

def main():
	numcases = readline()
	for i in xrange(int(numcases)):
		case(i + 1)

main()
