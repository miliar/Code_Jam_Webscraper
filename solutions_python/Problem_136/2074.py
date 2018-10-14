import time

ficheiro=open("input.in","r").read().split('\n');
 
for temp in range(1,int(ficheiro[0])+1):
	time = 0
	aux = ficheiro[temp].split(' ')
	cost = float(aux[0])
	bonus = float(aux[1])
	goal = float(aux[2])
	rate = 2
	
	while 1:
		ttgoal = goal/rate
		tibuy = cost/rate + goal/(rate+bonus)

		if ttgoal < tibuy:
			aux = ttgoal + time
			merda = str("%.7f" % aux)
			print("Case #"+str(temp)+': '+str(merda))
			break
		else:
			time = time + cost/rate
			rate = rate + bonus
