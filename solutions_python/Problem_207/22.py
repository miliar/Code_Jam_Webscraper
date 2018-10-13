from sys import stdin
readline = stdin.readline

T = int(readline())
for t in xrange(1, T+1):
	N, R, O, Y, G, B, V = map(int, readline().strip().split())
	
	if V > Y or G > R or O > B:
		print "Case #%d: IMPOSSIBLE" % t
		continue
	
	if V == Y and V != 0:
		if N == V+Y:
			ans = "VY"*(N/2)
			print "Case #%d: %s" % (t, ans)
		else:
			print "Case #%d: IMPOSSIBLE" % t
		continue
	
	if G == R and G != 0:
		if N == G+R:
			ans = "GR"*(N/2)
			print "Case #%d: %s" % (t, ans)
		else:
			print "Case #%d: IMPOSSIBLE" % t
		continue
	
	if O == B and O != 0:
		if N == O+B:
			ans = "OB"*(N/2)
			print "Case #%d: %s" % (t, ans)
		else:
			print "Case #%d: IMPOSSIBLE" % t
		continue
	
	if G:
		Rstrings = ["RG"*G + 'R'] + ['R']*(R-G-1)
	else:
		Rstrings = ['R']*R
	
	if V:
		Ystrings = ["YV"*V + 'Y'] + ['Y']*(Y-V-1)
	else:
		Ystrings = ['Y']*Y
	
	if O:
		Bstrings = ["BO"*O + 'B'] + ['B']*(B-O-1)
	else:
		Bstrings = ['B']*B
	
	#preference R>Y>B
	
	Rcount = len(Rstrings)
	Ycount = len(Ystrings)
	Bcount = len(Bstrings)
	
	if Rcount == max([Rcount, Ycount, Bcount]):
		ans = Rstrings[Rcount-1]
		Rcount -= 1
		ansprev = 'R'
	elif Ycount == max([Rcount, Ycount, Bcount]):
		ans = Ystrings[Ycount-1]
		Ycount -= 1
		ansprev = 'Y'
	else:
		ans = Bstrings[Bcount-1]
		Bcount -= 1
		ansprev = 'B'
	
	flag = True
	while Rcount + Ycount + Bcount:
		if ansprev == 'R' and Ycount+Bcount > 0:
			if Ycount > Bcount or ((Ycount == Bcount) and ans[0] == 'Y'):
				ans += Ystrings[Ycount-1]
				Ycount -= 1
				ansprev = 'Y'
			else:
				ans += Bstrings[Bcount-1]
				Bcount -= 1
				ansprev = 'B'
		
		elif ansprev == 'Y' and Rcount+Bcount > 0:
			if Rcount > Bcount or ((Rcount == Bcount) and ans[0] == 'R'):
				ans += Rstrings[Rcount-1]
				Rcount -= 1
				ansprev = 'R'
			else:
				ans += Bstrings[Bcount-1]
				Bcount -= 1
				ansprev = 'B'
		
		elif ansprev == 'B' and Rcount+Ycount > 0:
			if Rcount > Ycount or ((Rcount == Ycount) and ans[0] == 'R'):
				ans += Rstrings[Rcount-1]
				Rcount -= 1
				ansprev = 'R'
			else:
				ans += Ystrings[Ycount-1]
				Ycount -= 1
				ansprev = 'Y'
		else:
			print "Case #%d: IMPOSSIBLE" % t
			flag = False
			break
	
	if flag == False:
		continue
	if ans[0] == ans[-1]:
		print "Case #%d: IMPOSSIBLE" % t
	else:
		print "Case #%d: %s" % (t, ans)
