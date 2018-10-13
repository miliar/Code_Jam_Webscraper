
def needsextra(record):
	data = record.split(" ")
	levels = int(data[0])
	auidence = data[-1]
	digits = map(int, auidence.strip())
	num_needed = 0
	current_standup = 0
	for i in range(levels+1):
		if current_standup < i :
			num_needed += i - current_standup
			current_standup += i - current_standup
		current_standup += digits[i]
	return num_needed

if __name__=="__main__":
	filename = "A-large"
	with open(filename+'.in') as f:
		lines = f.readlines()
		num_of_tests = int(lines[0].strip())
		tests = lines[1:num_of_tests+1]
	results = map(needsextra, tests)
	with open(filename+'.out','w') as f:
		for i in range(num_of_tests):
			f.write("Case #%s: %s\n" % (i+1,results[i]))
