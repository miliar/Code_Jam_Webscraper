t = int(input())
for t_index in range(t):
	n, r, o, y, g, b, v = [int(i) for i in input().split()]
	tot_r = r + o + v
	tot_y = y + o + g
	tot_b = b + g + v
	if tot_r > n/2 or tot_y > n/2 or tot_b > n/2:
		print("Case #"+str(t_index+1)+": IMPOSSIBLE")
		continue
	s=""
	last = ""
	first = ""
	while r+y+b:
		if last == "":
			if b >= y and b >= r and b:
				b-=1
				last="B"
				first="B"
			elif r >= y and r >= b and r:
				r-=1
				last="R"
				first="R"
			elif y >= r and y >= b and y:
				y-=1
				last="Y"
				first="Y"
		elif first=="R" and last != "R" and r:
			r-=1
			last="R"
		elif first=="Y" and last != "Y" and y:
			y-=1
			last="Y"
		elif first=="B" and last != "B" and b:
			b-=1
			last="B"
		elif last=="R":
			if b > y and b:
				b-=1
				last="B"
			else:
				if y:
					y-=1
					last="Y"
		elif last=="Y":
			if r > b and r:
				r-=1
				last="R"
			else:
				if b:
					b-=1
					last="B"
		elif last=="B":
			if r > y and r:
				r-=1
				last="R"
			else:
				if y:
					y-=1
					last="Y"
		#else:
		#	s="IMPOSSIBLE"
		#	break
		s+=last
	#if s[0]==s[-1]:
	#	s="IMPOSSIBLE"
	print("Case #"+str(t_index+1)+": "+s)
