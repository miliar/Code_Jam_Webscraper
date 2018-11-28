fout = open("Dout.txt",'w')
fout.write('')
fout.close()

fin = open('D-large.in')
T = int(fin.readline())

for i in range(T):
	N = int(fin.readline())
	naomi = fin.readline().split()
	ken = fin.readline().split()

	naomi = sorted(naomi)
	ken = sorted(ken)

	war_wins=0
	dec_wins=0

	ken_war = ken[:]
	naomi_war = naomi[:]

	#War:
	for ni, n in enumerate(naomi_war):
		for ki, k in enumerate(ken_war):
			if k>n:
				ken_war.pop(ki)
				break
			elif (ki == len(ken_war)-1):
				ken_war.pop(ki)
				war_wins+=1
				break

	ken_dec = ken[:]
	naomi_dec = naomi[:]

	#Deceptive War:
	while len(naomi_dec)>=1:
		if (naomi_dec[-1]>ken_dec[-1]):
			dec_wins+=1
			naomi_dec.pop(-1)
			ken_dec.pop(-1)
		else:
			naomi_dec.pop(0)
			ken_dec.pop(-1)

	#write to output file:
	fout = open("Dout.txt",'a')

	fout.write('Case #%d: %d %d\n'%(i+1, dec_wins, war_wins))

	fout.close()



