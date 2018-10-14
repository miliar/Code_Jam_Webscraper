f = open('A-small-attempt2.in','r')
T = int(f.readline())
#print "T = " + str(T)#
b = 0
for i in range(T):
	first = int(f.readline())-1
	#print "first =" + str(first)#
	rows = []
	for i in range(4):
		r = f.readline().split()
		#print r #
		rows += [r]
	second = int(f.readline())-1
	#print "second = " + str(second) #
	#print rows[second] #
	rows2 =[]
	for i in range(4):
		r = f.readline().split()
		#print r#
		rows2 += [r]
	p = True
	res = []
	#print rows2[second]#
	for a in rows2[second]:
		#print a#
		#print rows[first]#
		if a in rows[first]:
			res += [a]
	if len(res)>1:
		p = False
		b+=1
		print 	"Case #" + str(b) +": Bad magician!"
	elif len(res) == 1:
		p = False
		b+=1
		print 	"Case #" + str(b) +": " + res[0]
	if p:
		b+=1
		print 	"Case #" + str(b) +": Volunteer cheated!"