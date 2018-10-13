import math

f = open('test2.txt', "r")

num = f.readline()
q = 1
for i in range(int(num)):
	c = 0
	a = f.readline().split(" ")

	for j in range(int(a[0]), int(a[1]) + 1):
		if str(j) == str(j)[::-1]:
			e = math.sqrt(j)
			if float(e).is_integer() and str(int(e)) == str(int(e))[::-1]:
				c+=1

	print "Case #" + str(q) + ": " + str(c)
	q+=1






f.close()











