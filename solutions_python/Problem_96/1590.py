#dancers.py
#Matt Lough - sifrawr@gmail.com

n = int(raw_input())

for i in range(n):
	p_nosuprise = 0
	p_suprise = 0
	
	inp = raw_input().split()
	googlers = int(inp[0])
	suprising = int(inp[1])
	target = int(inp[2])
	for x in range(googlers):
		cur = int(inp[3 + x])
		check = cur / 3
		if cur % 3 == 0:
			if check >= target:
				p_nosuprise += 1
			elif check > 0 and check + 1 >= target:
				p_suprise += 1
		elif cur % 3 == 1:
			if check + 1 >= target:
				p_nosuprise += 1
		elif cur % 3 == 2:
			if check + 1 >= target:
				p_nosuprise += 1
			elif check + 2 >= target:
				p_suprise += 1
	print "Case #%i: %i" % (i + 1, p_nosuprise + (min(suprising, p_suprise)))