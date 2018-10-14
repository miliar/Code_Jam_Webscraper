file = open("read.txt", 'r')
wfile = open("write.txt", 'w')
x = int(file.readline());
for k in xrange(x):
	num = int(file.readline().strip())
	lnum = list(str(num))
	lnum = map(int,lnum)
	bigger = True
	while bigger:
		bigger = False
		for no in xrange(len(lnum) - 1):
			if lnum[no] > lnum[no + 1]:
				bigger = True
				lnum[no] -= 1
				for mv in xrange(no + 1, len(lnum)):
					lnum[mv] = 9
	wfile.write("Case #" + str(k + 1) + ": " + str(int("".join(map(str,lnum)))))
	wfile.write("\n")