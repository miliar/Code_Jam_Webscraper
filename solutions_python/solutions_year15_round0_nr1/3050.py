def read(filename):
	data = open(filename, 'r').read().split('\n')
	return data[0], data[1:]


def solve(n, audi):
	res = 0

	for i in range(len(audi)):
		
		if audi[i] == 0: continue
		
		s = sum(audi[:i])
		# print s,res,i
		if s+res < i:
			res += i - (s + res)
	
	return res

filename = 'A-large.in'
ofile = filename.split('.')[0]+'.out'
wr = open(ofile, 'w')

t, data = read(filename)
test = 1
for row in data:
	if len(row) > 0:
		row = row.split(' ')
		n = int(row[0])
		audi = [int(elem) for elem in row[1]] 

		res = solve(n, audi)

		print "Case #%d: %d" % (test, res)
		wr.write("Case #%d: %d" % (test, res))
		if test != 100:
			wr.write('\n')

		test += 1