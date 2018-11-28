import math
f = open("/Users/sangypae/Desktop/gcj/a/A-test.in", 'r')
contents = f.read()
cases = int(contents.split("\n")[0])
contents = contents.split("\n")[1:]
for i in range(cases):
	r, c, w = map(int, contents[i].split(" "))
	if c % w == 0:
		c1 = c/w
	else:
		c1 = c/w+1
	ans = r*c1+(w-1)


	g = open("/Users/sangypae/Desktop/gcj/a/a-output.txt", 'a')
	g.write("Case #" + str(i+1)+": " + str(ans) + "\n")
	g.close()