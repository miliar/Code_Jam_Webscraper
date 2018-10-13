T = input()
int (T)
i = 1
while i <= T:
	scom=raw_input()
	Smax,S = (scom.split())
	Si=0
	ppl=0
	fpt=0
	for j in str(S):
		friend_ppl=0
		if ppl < Si:
			friend_ppl=Si-ppl
			ppl=Si
		ppl=ppl+int(j)
		Si = Si + 1
		fpt=fpt+friend_ppl
	print ("case #"+str(i)+": "+str(fpt))
	i += 1
#exit
