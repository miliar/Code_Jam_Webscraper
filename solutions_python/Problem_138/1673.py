f = open("/home/pietro/Scrivania/input", "rb")
outF = open("/home/pietro/Scrivania/output", "wb")

cases = int(f.readline())

for N in range(0, cases, 1):
	blocks = int(f.readline())

	naomi_w = [float(x) for x in f.readline().split()]
	ken_w = [float(x) for x in f.readline().split()]
	naomi_w.sort()
	ken_w.sort()

	ken_w2 = [x for x in ken_w]
	kenwar = 0
	for i in naomi_w:
		for j in range(0, len(ken_w2),1):
			if ken_w2[j]>i:
				ken_w2.remove(ken_w2[j])
				kenwar += 1
				break
				
	naomiwar = len(naomi_w)-kenwar

	naomiwin = 0

	while(len(naomi_w) > 0):
		naomi_lim = 0
		kenwin = 0
		
		
		for i in naomi_w:
			if i < ken_w[0]:
				kenwin+=1
		if kenwin > 0:
			ken_w = ken_w[:-kenwin]
			naomi_w = naomi_w[kenwin:]
		
		kenwin = 0

		for i in ken_w:
			if i > naomi_w[len(naomi_w)-1]:
				kenwin+=1
		if kenwin > 0:
			ken_w = ken_w[:-kenwin]
			naomi_w = naomi_w[kenwin:]
		
		
		for i in range(0, len(naomi_w), 1):
			if naomi_w[i] > ken_w[i]:
				naomi_lim+=1
			else:
				break
		
		if naomi_lim>0:
			naomi_w = naomi_w[naomi_lim:]
			ken_w = ken_w[naomi_lim:]
			naomiwin += naomi_lim


	outF.write("Case #"+str(N+1)+": "+str(naomiwin)+" "+str(naomiwar)+"\n")

f.close()
outF.close()
