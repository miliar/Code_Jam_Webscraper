filename = 'B-small-attempt0.in'
f = open(filename,'r')

T = int(f.readline())
for t in range(1,T+1):
	print "Case #%d:" % t,
	N,R,O,Y,G,B,V = map(int,f.readline().split())
	if (max(R,Y,B,O,G,V)>N/2 or O > B or G > R or V > Y):
		print "IMPOSSIBLE"
	elif (R+B<Y or R+Y<B or Y+B<R):
		print "IMPOSSIBLE"
	else:
		if R != 0:
			ans = "R"
			R-=1
		elif B != 0:
			ans = "B"
			B-=1
		else:
			ans = "Y"
			Y-=1
		while R+B+Y>0:
			if R == max(R,B,Y):
				if ans[-1] == "R":
					if B > Y:
						ans += "B"
						B-=1
					else:
						ans += "Y"
						Y-=1
				else:
					ans += "R"
					R-=1
			elif B == max (R,B,Y):
				if ans[-1] == "B":
					if R > Y:
						ans += "R"
						R-=1
					else:
						ans += "Y"
						Y-=1
				else:
					ans += "B"
					B-=1
			else:
				if ans[-1] == "Y":
					if R > B:
						ans += "R"
						R-=1
					else:
						ans += 'B'
						B-=1
				else:
					ans += "Y"
					Y -= 1
		print ans