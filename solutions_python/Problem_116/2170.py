f = open('abc.txt', 'r')
out = open('a-output.txt', 'w')
total = f.readline()
for tt in range(int(total)):
	q = f.readline()
	w = f.readline()
	e = f.readline()
	r = f.readline()
	
	a = q.replace("T","X")
	b = w.replace("T","X")
	c = e.replace("T","X")
	d = r.replace("T","X")
	
	#print a
	#print b
	#print c
	#print d
	
	if (a[0] == "X" and a[1] == "X" and a[2] == "X" and a[3] == "X") or (b[0] == "X" and b[1] == "X" and b[2] == "X" and b[3] == "X") or (c[0] == "X" and c[1] == "X" and c[2] == "X" and c[3] == "X") or (d[0] == "X" and d[1] == "X" and d[2] == "X" and d[3] == "X") or (a[0] == "X" and b[0] == "X" and c[0] == "X" and d[0] == "X") or (a[1] == "X" and b[1] == "X" and c[1] == "X" and d[1] == "X") or (a[2] == "X" and b[2] == "X" and c[2] == "X" and d[2] == "X") or (a[3] == "X" and b[3] == "X" and c[3] == "X" and d[3] == "X") or (a[0] == "X" and b[1] == "X" and c[2] == "X" and d[3] == "X") or (a[3] == "X" and b[2] == "X" and c[1] == "X" and d[0] == "X"):
		out.write("Case #" + str(tt+1) + ": " + "X won" + "\n")
	else:	
		a = q.replace("T","O")
		b = w.replace("T","O")
		c = e.replace("T","O")
		d = r.replace("T","O")
		if (a[0] == "O" and a[1] == "O" and a[2] == "O" and a[3] == "O") or (b[0] == "O" and b[1] == "O" and b[2] == "O" and b[3] == "O") or (c[0] == "O" and c[1] == "O" and c[2] == "O" and c[3] == "O") or (d[0] == "O" and d[1] == "O" and d[2] == "O" and d[3] == "O") or (a[0] == "O" and b[0] == "O" and c[0] == "O" and d[0] == "O") or (a[1] == "O" and b[1] == "O" and c[1] == "O" and d[1] == "O") or (a[2] == "O" and b[2] == "O" and c[2] == "O" and d[2] == "O") or (a[3] == "O" and b[3] == "O" and c[3] == "O" and d[3] == "O") or (a[0] == "O" and b[1] == "O" and c[2] == "O" and d[3] == "O") or (a[3] == "O" and b[2] == "O" and c[1] == "O" and d[0] == "O"):
			out.write("Case #" + str(tt+1) + ": " + "O won" + "\n")
		else:
			if (a[0] == "." or a[1] == "." or a[2] == "." or a[3] == "." or b[0] == "." or b[1] == "." or b[2] == "." or b[3] == "." or c[0] == "." or c[1] == "." or c[2] == "." or c[3] == "." or d[0] == "." or d[1] == "." or d[2] == "." or d[3] == "."):
				out.write("Case #" + str(tt+1) + ": " + "Game has not completed" + "\n")
			else:
				out.write("Case #" + str(tt+1) + ": " + "Draw" + "\n")
		

	
	f.readline()
	#out.write("Case #" + str(tt+1) + ": " + str(count) + "\n")