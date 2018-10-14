
def solve(name, length, log):
	count = 0

	for i in range(0, (len(name) - length) + 1):
		log.write("first = %c\n" % name[i])
		for j in range(i + length - 1, len(name)):
			log.write("last = %c\n" % name[j])
			conscount = 0
			log.write(name[i : j + 1] + '\n')
			for s in name[i : j + 1]:
				if s not in ['a', 'e', 'i', 'o', 'u']:
					log.write(s + ' is a consonant\n')
					conscount += 1
				else:
					conscount = 0
				
				if conscount == length:
					break
			
			if conscount == length:
				log.write(name[i : j + 1] + " has consonants\n")
				count += 1
					
	return count
		
def run(filename):
	f = open(filename + '.in', 'r')
	o = open(filename + '.out', 'w')
	log = open(filename + '.log' , 'w')

	for i in range(1, int(f.readline()) + 1):
		name, length = [m for m in f.readline().strip().split(" ")]
		length = int(length)
		answer = "Case #%d: %d" % (i, solve(name, length, log))
		o.write(answer + '\n')
		print answer
	f.close()
	o.close()
	log.close()

run('sample')
