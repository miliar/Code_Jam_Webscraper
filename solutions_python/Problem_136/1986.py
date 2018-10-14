kacdefa = input()
index = 1
while(index <= kacdefa):
	satir = raw_input().split(" ")
	C = float(satir[0])
	F = float(satir[1])
	X = float(satir[2])
	zaman = []
	suankiUretim = 2.0
	bodos = 0.0
	yatirim = 0.0
	while( True ):
		bodos = X/suankiUretim
		yatirim = C/suankiUretim + X/(suankiUretim+F)
		if(bodos <= yatirim):
			#print "bodos gidiyoz cunku %s, %s"%(bodos, yatirim)
			zaman.append(X/suankiUretim)
			break;
		else:
			#print "yatirim gidiyoz cunku %s, %s"%(bodos, yatirim)
			zaman.append(C/suankiUretim)
			suankiUretim = suankiUretim + F
			continue;
	print "Case #%s: %.7f"%(index,sum(zaman))


	index = index +1
