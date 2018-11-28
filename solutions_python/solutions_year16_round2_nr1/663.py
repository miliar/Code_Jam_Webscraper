def solve(S):
	phone = []
	even = {"ZERO": ("Z", 0), "TWO": ("W", 2), 
			"FOUR": ("U", 4), "SIX": ("X", 6), "EIGHT": ("G", 8)}
	odd =  {"ONE": ("O", 1), "THREE": ("H", 3), "FIVE": ("F", 5), "SEVEN": ("S", 7)}
	nine = {"NINE": ("N", 9)}
	for nr in even:
		while S.find(even[nr][0]) > -1:
			phone.append(even[nr][1])
			for c in nr:
				S = S.replace(c, '', 1)
	for nr in odd:
		while S.find(odd[nr][0]) > -1:
			phone.append(odd[nr][1])
			for c in nr:
				S = S.replace(c, '', 1)
	for nr in nine:
		while S.find(nine[nr][0]) > -1:
			phone.append(nine[nr][1])
			for c in nr:
				S = S.replace(c, '', 1)
	phone.sort()
	return ''.join(str(nr) for nr in phone)

t = int(raw_input())
for i in xrange(1, t + 1):
  S = raw_input()
  print "Case #{}: {}".format(i, solve(S))