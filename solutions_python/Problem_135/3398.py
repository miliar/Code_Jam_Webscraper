caso = 1
i1 = input()
while caso<=i1:
	i2 = input()
	linha = 0
	linha1 = raw_input()
	linha2 = raw_input()
	linha3 = raw_input()
	linha4 = raw_input()

	i3 = input()
	linha21 = raw_input()
	linha22 = raw_input()
	linha23 = raw_input()
	linha24 = raw_input()
	
	if i2==1:
		x = linha1.split()
	elif i2==2:
		x = linha2.split()
	elif i2==3:
		x = linha3.split()
	elif i2==4:
		x = linha4.split()
	s = set()
	s.add(int(x[0]))
	s.add(int(x[1]))
	s.add(int(x[2]))
	s.add(int(x[3]))

	if i3==1:
		x2 = linha21.split()
	elif i3==2:
		x2 = linha22.split()
	elif i3==3:
		x2 = linha23.split()
	elif i3==4:
		x2 = linha24.split()
	s2 = set()
	s2.add(int(x2[0]))
	s2.add(int(x2[1]))
	s2.add(int(x2[2]))
	s2.add(int(x2[3]))

	d = s.intersection(s2)
	d2 = len(d)	
	caso2 = str(caso)
	if (d2 == 1):
		resp2 = d.pop()
		resp  = str(resp2)
		print "Case #"+caso2+": "+ resp
		
	elif (d2 > 1):
		print "Case #"+caso2+": Bad magician!"
	else:
		print "Case #"+caso2+": Volunteer cheated!"

	

	caso+=1 
