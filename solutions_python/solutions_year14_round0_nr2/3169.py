with open('input.txt') as inpt:
	lines = inpt.readlines()
	tests = int(lines[0])
	with open('output.txt','w') as out:
		for i in xrange(tests):
			rate = 2
			c, f, x = lines[i+1].split()
			c, f, x = float(c), float(f), float(x)
			seconds = x / rate
			newseconds = c / rate + x / (rate + f)
			timepassed = c / rate
			while seconds > newseconds:
				rate += f
				seconds = newseconds
				newseconds = timepassed + c / rate + x / (rate + f)
				timepassed += c / rate
			print >> out, 'Case #%d:' % (i+1) , '%.7f' % seconds