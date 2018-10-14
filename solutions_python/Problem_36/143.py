search = 'welcome to code jam'

cache = {}
def find_from(search, line, start=0):
	if (search, line, start) in cache:
		return cache[(search, line, start)]
	result = 0
	pos = line.find(search[0], start)
	if pos > -1:
		if len(search)==1:
			result = 1
		else:
			result = find_from(search[1:], line[pos+1:])
		result += find_from(search, line[pos+1:])
	cache[(search, line, start)] = result
	return result

def parse(file):
	lines = open(file).readlines()
	lines = [line.strip() for line in lines]
	length = int(lines[0])
	
	for i, line in enumerate(lines[1:length+1]):
		x = '%04d' % find_from(search, line)
		print('Case #%s: %s' % (i+1, x[-4:]))
		
parse('C-large.in')