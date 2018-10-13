inputfile = open('D-large.in.txt')
outputfile = open('result2.txt','w')

no_of_tests = int(inputfile.readline())

for t in range(no_of_tests):
	n =  int(inputfile.readline())
	naomis_blocks = map(float,inputfile.readline().split())
	kens_blocks = map(float,inputfile.readline().split())
	naomis_blocks.sort()
	kens_blocks.sort()
	
	kens_blocks2 = list(kens_blocks)
	naomis_blocks2 = list(naomis_blocks)
	y=0
	z=0	
	# Deceit
	while len(naomis_blocks) > 0:
		n_small = naomis_blocks.pop(0)
		# find next smallest in kens
		nearest =10.0
		index = 0
		nearest_index = 0
		# could binary search for speed
		for block in kens_blocks:
			if block > n_small and block < nearest:
				nearest = block
				nearest_index = index
			index+=1
			
		if block < n_small:
		 	z+=1

		kens_blocks.pop(nearest_index)
		
	while len(naomis_blocks2) > 0:
		n_small = naomis_blocks2.pop(0)
		k_large = kens_blocks2[0]

		if k_large < n_small:
		 	y+=1
			kens_blocks2.pop(0)
		else:
			kens_blocks2.pop()

			
					
	print >>outputfile, "Case #%d: %d %d" % (t+1,y,z)


outputfile.close()


