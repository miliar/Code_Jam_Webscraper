filename="A-large.in"
with open("out_large.txt",'w') as out:
	with open(filename) as f:
		cases = int(f.readline())	
		for i in xrange(cases):
			line = f.readline()
			friends = 0
			audience = 0
			for ii,s in enumerate(line.split(' ')[-1][:-1]):
				p_s = int(s)
				audience += p_s
				if(audience < ii+1):
					add_pos = ii+1-audience
					friends += add_pos
					audience += add_pos
			s = "Case #"+ str(i+1)+ ": "+str(friends)+"\n"
			out.write(s)