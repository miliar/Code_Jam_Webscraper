fi = open("test1.txt", "r")
fo = open("output","w")
count = int(fi.readline())
for i in range(0,count):
	total = 0
	need = 0
	temp = fi.readline()
	shymax = int(temp.split()[0])
	aud = temp.split()[1]
	for j in range(0,shymax+1):
		if j > total:
			need = need + 1
			total = total + 1
		total = total + int(aud[j])
	fo.write("Case #{0}: {1}\n".format(i+1, need))

fi.close()
fo.close()