f = open("./dataset", "rb")
ofp = open("./output", "wb")

cases = int(f.readline())

for N in range(0, cases, 1):
	blocks = int(f.readline())

	wnaomi = [float(x) for x in f.readline().split()]
	wken = [float(x) for x in f.readline().split()]
	wnaomi.sort()
	wken.sort()

	wken2 = [x for x in wken]
	kenwar = 0
	for i in wnaomi:
		for j in range(0, len(wken2),1):
			if wken2[j]>i:
				wken2.remove(wken2[j])
				kenwar += 1
				break
				
	naomiwar = len(wnaomi)-kenwar

	naomiwin = 0

	while(len(wnaomi) > 0):
		naomiwinparziale = 0
		kenwin = 0
		
		
		for i in wnaomi:
			if i < wken[0]:
				kenwin+=1
		if kenwin > 0:
			wken = wken[:-kenwin]
			wnaomi = wnaomi[kenwin:]
		
		kenwin = 0

		for i in wken:
			if i > wnaomi[len(wnaomi)-1]:
				kenwin+=1
		if kenwin > 0:
			wken = wken[:-kenwin]
			wnaomi = wnaomi[kenwin:]
		
		
		for i in range(0, len(wnaomi), 1):
			if wnaomi[i] > wken[i]:
				naomiwinparziale+=1
			else:
				break
		
		if naomiwinparziale>0:
			wnaomi = wnaomi[naomiwinparziale:]
			wken = wken[naomiwinparziale:]
			naomiwin += naomiwinparziale


	ofp.write("Case #"+str(N+1)+": "+str(naomiwin)+" "+str(naomiwar)+"\n")

f.close()
ofp.close()
