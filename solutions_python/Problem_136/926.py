
def main(filePath):
	answer = open('answers','w')
	with open(filePath, 'r') as fd:
		numCase = int(float(fd.readline().strip()))

		for i in range(numCase):
			values = fd.readline().strip().split()
			filter(None, values)
			assert(len(values) == 3)
			c = float(values[0])
			f = float(values[1])
			x = float(values[2])

			farms = 0
			run = True

			result = x / (2 + (farms*f))
			time = c / 2
			withMoreFarm = (x / (2 + ((farms+1)*f)) ) + time
			while result > withMoreFarm:
				farms += 1
				result = x / (2 + (farms*f)) + time
				time += c / (2 + farms*f)
				withMoreFarm = x / (2 + ((farms+1)*f)) + time

			answer.write('Case #%s: %s\n' % ((i+1),str(round(result,7))))




if __name__ == '__main__':
	import sys
	if len(sys.argv) > 1:
		main(sys.argv[1])
	else:
		raise Exception('[-] Missing arg')