
fin = open("A-large.in", 'r')
fout = open("A-large.out", 'w')

ntests = int(fin.readline())

for t in range(0, ntests):
	info = fin.readline().split()
	max_shy = int(info[0])
	ppl_info = info[1]

	ppl_standing = 0
	ppl_to_add = 0
	for i in range(0, max_shy+1):
		num_ppl = int(ppl_info[i])
		ppl_standing = ppl_standing + num_ppl
		if ppl_standing <= i:
			ppl_to_add = ppl_to_add + 1
			ppl_standing = ppl_standing + 1

	fout.write("Case #" + str(t+1) + ": " + str(ppl_to_add) + "\n")

fin.close()
fout.close()


