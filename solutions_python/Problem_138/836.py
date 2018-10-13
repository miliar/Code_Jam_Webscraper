fp=open("D-large.in","r")
ptr=open("output-P4.txt","w")
num_cases=int(fp.readline())

for i in range(num_cases):
	n=int(fp.readline())
	naomi_intblockblock=fp.readline().split()
	naomi_intblock=map(float,naomi_intblockblock)
	dw_naomi_intblock=naomi_intblock[:]

	ken_intblockblock=fp.readline().split()
	ken_intblock=map(float,ken_intblockblock)
	dw_ken_intblock=ken_intblock[:]

	ken_intblock.sort()

	deceitwar,war=0,0
	j=0
	for j in range(n):
		if max(ken_intblock)>naomi_intblock[j]:
			for k in ken_intblock:
				if k>naomi_intblock[j]:
					ken_intblock.remove(k)
					break
		else:
			ken_intblock.remove(min(ken_intblock))
			war+=1

		if min(dw_naomi_intblock)<min(dw_ken_intblock):
			dw_ken_intblock.remove(max(dw_ken_intblock))
			dw_naomi_intblock.remove(min(dw_naomi_intblock))
		else:
			dw_ken_intblock.remove(min(dw_ken_intblock))
			dw_naomi_intblock.remove(min(dw_naomi_intblock))
			deceitwar+=1

	ptr.write("Case #{}: {} {}\n".format(i+1,deceitwar,war))
