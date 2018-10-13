import fileinput

cache = {}

def are_recycled(a, b):
	if (a,b) in cache:
		return cache[(a,b)]
	
	str_a = str(a)
	str_b = str(b)

	len_a = len(str_a)
	len_b = len(str_b)

	if len_a != len_b:
		cache[(a,b)] = False
		return False

	for i in range(len_a - 1):
		shift = i + 1

		if str_a[shift:] + str_a[:shift] == str_b:
			cache[(a,b)] = True
			return True

limit = -1

for i, line in enumerate(fileinput.input()):
	if i == 0:
		limit = int(line)
		continue
	
	if limit != -1 and i > limit:
		continue
	
	limits = map(int, line.split())
	count = 0
	
	j = limits[0]
	
	while j <= limits[1]:
		k = j+1
		while k <= limits[1]:
			if are_recycled(j, k):
				count += 1
			k += 1

		j += 1
		
	print "Case #"+str(i)+":",count
