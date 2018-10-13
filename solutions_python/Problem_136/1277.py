fi = open("input.txt")
fo = open("output.txt", "r+")

cases = int(fi.readline())

for c in range(cases):
	settings = fi.readline().rstrip().split()
	farmcost = float(settings[0])
	farmprod = float(settings[1])
	
	goal = float(settings[2])

	cookies = 0.0
	production = 2.0



	farmprofit = farmcost/farmprod

	t = 0

	while(True):
		timeleft = (goal - cookies)/production
		timefarm = (farmcost - cookies)/production
		
		if(cookies >= farmcost):
			if(farmprofit < timeleft):
				cookies -= farmcost
				production += farmprod
			else:
				t += timeleft
				break


		else:
			t += timefarm
			cookies = farmcost

	fo.write("Case #" + str(c + 1) + ": " + str(t) + "\n")