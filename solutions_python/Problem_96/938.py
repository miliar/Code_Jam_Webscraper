import sys

if __name__ == "__main__":
	nb = int(sys.stdin.readline())
	cpt = 1
	
	while cpt <= nb:
		line = sys.stdin.readline().replace('\n', '')
		l = line.split(' ')
		l = [int(i) for i in l]
		
		nbGooglers = l[0]
		nbSurprise = l[1]
		note = l[2]
		total = 0
		min = (note+((note-1)*2))
		surpr = (note+((note-2)*2))
		
		for n in l[3:]:
			if note == 0:
				total = nbGooglers
				break
			else:
				if n > 0:					
					if n >= min:
						total += 1
					elif n >= surpr and nbSurprise > 0:
						total += 1
						nbSurprise -= 1
		
		print 'Case #'+str(cpt)+': '+str(total)
		
		cpt += 1
	