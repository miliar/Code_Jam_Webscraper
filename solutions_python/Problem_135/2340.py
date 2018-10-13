from sys import argv
scriptname, file = argv
a = open(file, "r")
b = open("small.in", "w")
num = int(a.readline().strip("\n"))
l1, l2 = 0, 0
c = []
out = ""
for x in xrange(num):
	l1 = int(a.readline().strip("\n"))-1
	ar, ar2 = [], []
	for y in range(0, 4):
		ar.append(a.readline().strip("\n").split(" "))
	l2 = int(a.readline().strip("\n"))-1
	for y in range(0, 4):
		ar2.append(a.readline().strip("\n").split(" "))
	i = ""
	c = [i for i in ar[l1] if i in ar2[l2]]
	print len(c)
	if len(c) > 1:
		out = "Bad magician!"
	if len(c) ==1:
		out = c[0]
	if len(c) ==0:
		out = "Volunteer cheated!"
	print out
	b.write("Case #"+ str(x+1) + ": " + out+ "\n")
	
			
		