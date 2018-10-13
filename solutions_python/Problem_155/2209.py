f    = open("input")
T    = int(f.readline())
line = 1

while(line != T+1):
	str_ = ""
	c = f.read(1)
	while (c != ' '):
		str_ += c
		c = f.read(1)
	Smax = int(str_)

	# Read shyness table
	S    = []
	nb   = 0
	sum_ = 0
	p    = int(f.read(1))
	S.append(p)
	if (p == 0):
		nb = nb + 1 #at least one person with shyness level 0
	i    = 1        #counter of shyness
	sum_ = p + nb   #sum of people

	c    = f.read(1)
	while (c != '\n'):
		p    = int(c)
		#print("SHYNESS:" + str(i) + ", NB:"+ str(p) + ", SUM:" + str(sum_)) 
		if (sum_ <= i):
			#print("Added "+ str(i-sum_)+" members")
			nb   = nb + (i - sum_)
			sum_ = sum_ + (i - sum_)
		S.append(p)
		sum_ = sum_ + p
		i = i + 1
		c = f.read(1)
	print("Case #"+str(line)+": "+str(nb))
	line = line + 1
f.close()


