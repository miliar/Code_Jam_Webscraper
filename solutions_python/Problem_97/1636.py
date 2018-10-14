
def variations(n):
	ret = []


	if len(n) == 1:
		ret.append(n[0])
	elif len(n) == 2:
		return [
				int(n[0] + n[1]),
				int(n[1]+ n[0]),
				]
	elif len(n) == 3:
		return [
				int(n[0] + n[1] + n[2] + n[2]),
				int(n[1]+ n[2] + n[0]),
				int(n[2]+ n[0] + n[1]),				
				]
	elif len(n) == 4:
		return [
				int(n[0] + n[1] + n[2] + n[3]),
				int(n[1]+ n[2] + n[3] + n[0]),
				int(n[2]+ n[3] + n[0] + n[1]),				
				int(n[3]+ n[0] + n[1] + n[2]),				
				]

	return ret
def calcuate(i, s):
	spl = s.split(' ')
	min = int(spl[0])
	max = int(spl[1])
	count = 0
	j = 0
	for n in xrange(min,max):
		for m in list(set(variations( "%d" % n))):						
			if min <= n < m <= max:
				j += 1
				# print "%d\t%d" % (n,m)
				count += 1	
	print "%d %d == %d" % (min, max, count)
	s = '--'.join(spl)
	return "Case #%d: %d\n" % (i,count)

i = 0
output = ""
lines = open("sample.inp.txt",'r').readlines()
for s in lines:
	i = i + 1
	output += calcuate(i, s)

print output

open('result.out','w').write(output)