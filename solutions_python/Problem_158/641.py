f = open("/Users/sangypae/Desktop/gcj/D-small-attempt3.in", 'r')
contents = f.read()
cases = int(contents.split("\n")[0])
contents = contents.split("\n")[1:]
for i in range(cases):
	x, r, c = map(int, contents[i].split(" "))
	if r*c % x == 0:
		if x == 1 or x == 2:
			ans = "GABRIEL"
		elif x == 3:
			if r == 1 or c == 1:
				ans = "RICHARD"
			else:
				ans = "GABRIEL"
		elif x == 4:
			if r <= 2 or c <= 2:
				ans = "RICHARD"
			else:
				ans = "GABRIEL"
	else:
		ans = "RICHARD"


	g = open("/Users/sangypae/Desktop/gcj/d-output.txt", 'a')
	g.write("Case #" + `i+1`+": " + ans + "\n")
	g.close()