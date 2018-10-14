
def main(filePath):
	answer = open('answers','w')
	with open(filePath, 'r') as f:
		numCase = int(float(f.readline().strip()))

		for case in range(numCase):
			firstChoice = int(float(f.readline().strip()))
			firstArrangement = []
			for i in range(4):
				try:
					firstArrangement.append(f.readline().strip().split())
					#filter(None,firstArrangement[i])
				except:
					raise Exception("[-] Missing line in 1st arrangement.")

			secondChoice = int(float(f.readline().strip()))
			secondArrangement = []
			for i in range(4):
				try:
					secondArrangement.append(f.readline().strip().split())
					#filter(None,secondArrangement[i])
				except:
					raise Exception("[-] Missing line in 2nd arrangement.")
			
			possible = [x for x in secondArrangement[secondChoice-1] if x in firstArrangement[firstChoice-1]]
			
			result = ""
			if len(possible) > 1:
				result = "Bad magician!"
			elif not possible:
				result = "Volunteer cheated!"
			else:
				result = str(possible[0])

			answer.write('Case #%s: %s\n' % ((case+1),result))

			## DEBUG
			#print(firstArrangement[firstChoice-1])
			#print(secondArrangement[secondChoice-1])
			#print(possible)
	
	answer.close()




if __name__ == '__main__':
	import sys
	if len(sys.argv) > 1:
		main(sys.argv[1])
	else:
		raise Exception('[-] Missing argument.')