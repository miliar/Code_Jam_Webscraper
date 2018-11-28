def codeJam(fil):
	cases = int(fil.readline())
	input = ""
	for x in range(1, cases + 1):
		input = fil.readline().split()
		number_added = prima_donna([int(y) for y in input.pop()], input.pop())
		print "Case #" + str(x) + ": " + str(number_added)

def prima_donna(people, max_level):
	number_added = 0
	total = 0
	for s in range(len(people)):
		while total < s:
			total += 1
			number_added += 1
		total += people[s]
	return number_added

fil = open('A-large.in')
codeJam(fil)