filename1 = "D-large.in.txt"
#filename1 = "Input.txt"
filename2 = "Output.txt"

with open(filename2,'w') as g:
	with open(filename1,'r') as f:
		T = int(f.readline())
		for i in range(1,T + 1):
			N = int(f.readline())
			Nscore = 0
			Nai = f.readline().split()
			Ken = f.readline().split()
			for j in range(len(Nai)):
				Nai[j] = float(Nai[j])
				Ken[j] = float(Ken[j])
			Nai.sort()
			Ken.sort()
			Naicheat = list(Nai)
			Kencheat = list(Ken)
			for j in Nai:
				if j > Ken[len(Ken) - 1]:
					break
				else:
					for k in Ken:
						if k > j:
							Ken.remove(k)
							break
			z = len(Ken)

			y = 0
			for j in Naicheat:	
				for k in Kencheat:
					if j > k:
						Kencheat.remove(k)
						y += 1
						break
			g.write("Case #%s: %s %s\n" % (i, y, z))