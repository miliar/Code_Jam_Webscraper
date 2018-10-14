import string
f = open("B-large.in",'r')
g = open("output.txt",'w')

lines = f.readlines()

t = lines[0]
# print t
t = int(t)

for i in range(0,t):
	line = lines[i+1]
	line = string.split(line," ")
	n = int(line[0])
	s = int(line[1])
	p = int(line[2])
	# print n,s,p
	count = 0
	for j in range(0,n):
		tp = int(line[j+3])
		# print tp
		if tp%3==0:
			x = tp/3
			# print x				
			if x>=p:
				count = count+1
				# print count
			elif s>0 and x!=0:
				x = x+1
				s = s-1
				# print x,s,"surprising"
				if x>=p:
					count = count+1
					# print count
				else:
					s=s+1
		elif (tp-1)%3 == 0:
			x = (tp-1)/3 + 1
			# print x
			if x>=p:
				count = count+1
				# print count
		else:
			x = (tp-2)/3 + 1
			# print x
			if x>=p:
				count = count+1
				# print count
			elif s>0:
				x = x+1
				s = s-1
				# print x,s,"surprising"
				if x>=p:
					count = count+1
					# print count
				else:
					s=s+1
	s = "Case #" + str(i+1) + ": " + str(count) + "\n"
	g.write(s)
g.close()
f.close()
