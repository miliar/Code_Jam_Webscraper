teste = 1
t = input()
while teste<=t:
	i = raw_input()
	l = i.split()
	c = float(l[0])
	f = float(l[1])
	x = float(l[2])
	f2 = 2
	melhor = x/f2
	prod = 0 
	while(1):
		prod = prod+c/f2
		f2 = f+f2
		tempo = x/f2+prod
		if tempo < melhor:
			melhor = tempo
		else:
			break
	tstr = str(teste)
	mstr = str(melhor)
	print "Case #"+tstr+": "+mstr
	teste = teste+1
			
			
		
			
