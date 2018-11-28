f = file("A-large.in")
data = f.readlines()
f.close()

num_lines = int(data[0])

for num in range(1, num_lines+1):
	list = data[num].split(' ')
	n = int(list[0])
	k = int(list[1])
	print "Case #" + str(num) + ":", 
	if (k+1)%(2**n) == 0:
		print "ON"
	else:
		print "OFF"
