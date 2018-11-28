o = open("/Users/mklein16/Desktop/gcj/B-large.in", 'r')
contents = o.read()
cases = int(contents.split("\n")[0])
contents = contents.split("\n")
for i in range(cases):
	c, f, x = contents[i+1].split(" ")
	c = float(c)
	f = float(f)
	x = float(x)
	cps = 2
	secs = 0
	cookies = 0
	while cookies < x: 
		if (c-cookies) > 0:
			diff = c-cookies
		else:
			diff = 0
		if (diff/cps+x/(cps+f)) < (x-cookies)/cps: 
			if cookies < c:
				cookies = c #500
				secs += (c-cookies)/cps #250
			else:
				cookies -= c #0
				secs += c/cps #83.3333333
				cps += f #6
		else:
			secs += (x-cookies)/cps
			cookies = x
	o.close()
	g = open("/Users/mklein16/Desktop/gcj/output.txt", 'a')
	g.write("Case #" + `i+1`+": " + `secs` + "\n")
	g.close()