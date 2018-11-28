import sys

if __name__ == "__main__":
	nb = int(sys.stdin.readline())
	cpt = 1
	res = 0
	
	while cpt <= nb:
		compteur = 0
		mat1 = []
		mat2 = []
		answer1 = int(sys.stdin.readline().replace('\n', ''))
		for x in range(4):
			mat1.append(sys.stdin.readline().replace('\n', '').split(' '))
		answer2 = int(sys.stdin.readline().replace('\n', ''))
		for x in range(4):
			mat2.append(sys.stdin.readline().replace('\n', '').split(' '))
		l1 =  mat1[answer1-1]
		l2 =  mat2[answer2-1]
		for i in l1:
			if i in l2:
				compteur += 1
				res = i
				
		if compteur == 1:
			print 'Case #'+str(cpt)+': '+res
		elif compteur > 1:
			print 'Case #'+str(cpt)+': Bad magician!'
		else:
			print 'Case #'+str(cpt)+': Volunteer cheated!'
			
		cpt += 1