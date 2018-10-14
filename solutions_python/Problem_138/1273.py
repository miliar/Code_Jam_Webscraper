t = int(raw_input())

for i in range(1,t+1):
	
	n = int(raw_input())
	
	line = raw_input().split()
	naomi = []
	for j in range(0,n):
		naomi.append(float(line[j]))
	
	line = raw_input().split()
	ken = []
	for j in range(0,n):
		ken.append(float(line[j]))
	
	naomi = sorted(naomi)
	ken = sorted(ken)
	
	ind_ken = 0
	ind_naomi = 0
	end = False
	while ind_ken != n:
		while ken[ind_ken] < naomi[ind_naomi]:
			ind_ken += 1
			if ind_ken == n:
				end = True
				break
		if end:
			break
		ind_naomi += 1
		ind_ken += 1
	
	w = len(naomi) - ind_naomi
	
	dw = 0
	while len(ken) > 0:
		if ken[len(ken) - 1] < naomi[len(naomi) - 1]:
			dw += 1
			ken.pop()
			naomi.pop()
		else:
			ken.pop()
			naomi.pop(0)
	
	
	str = "Case #%d: %d %d" % (i, dw, w)
	print str