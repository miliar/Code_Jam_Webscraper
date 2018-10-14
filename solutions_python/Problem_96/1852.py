# Author: mfazal saintfiends@gmail.com

"""
4 # test cases
3 1 5 	15 13 11 			= 3# No.of googlers, surprising triplets, p, # # # #..
3 0 8 	23 22 21 			= 2 
2 1 1 	8 0      			= 1
6 2 8 	29 20 8 18 18 21	 = 3
"""
def get_count(scores):
	scores = scores.split()

	number_of_googlers = int(scores.pop(0))
	surprising_triplets = int(scores.pop(0))
	p = int(scores.pop(0))
	count = 0
	rounds = []

	for num in scores:
		num = int(num)
		even_score = num / 3
		rem = num % 3
		triplets =[even_score, even_score, even_score]
		i = 0
		while rem > 0:
			triplets[i] += 1
			rem -= 1
			i += 1
		rounds.append(triplets)


	rounds = sorted(rounds, key=sum, reverse=True)


	for i, triplets in enumerate(rounds):

		triplets = sorted(triplets)
		c, b, a = triplets


		if a >= p and 3 - (i+1) >= surprising_triplets:
			count += 1
		elif surprising_triplets:
			if surprising_triplets > 0:

				if b - 1 >= 0  and a + 1 <= 10 and ((a + 1) - (b - 1)) < 3: # problem
					surprising_triplets -= 1
					rounds[i] = [a + 1, b - 1, c]
					a = a + 1
					b = b - 1
				elif c - 1 >=0 and b + 1 <= 10 and ((b + 1) - (c - 1)) < 3:
					surprising_triplets -= 1
					rounds[i] = [a, b + 1, c - 1]
					b = b + 1
					c = c - 1

			if a >= p:
				count += 1


	return count


if __name__ == '__main__':

	problem = 'B'			
	attempt = 6 

	f = open("%s-small-attempt%d.in"%(problem, attempt), 'r')
	f.next() #skip top line
	with open("%s-small-attempt%d.out"%(problem, attempt), 'w') as out:
		for i, line in enumerate(f):
			out.write("Case #%d: %s\n" % (i+1, str(get_count(line)) ))

	f.close()
