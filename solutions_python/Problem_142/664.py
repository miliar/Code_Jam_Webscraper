
def case():
	num = int(input())

	strings = []

	for i in range(num):
		string = input()
		converted = []
		last = ""
		amount = 0
		for c in string:
			if c != last:
				converted.append((last, amount))
				last = c
				amount = 1
			else:
				amount += 1
		converted.append((last, amount))

		strings.append(converted)

	for a in strings:
		for b in strings:
			if len(a) != len(b):
				print("Fegla Won")
				return
			for c1, c2 in zip(a, b):
				if c1[0] != c2[0]:
					print("Fegla Won")
					return

	pituudet = [[i[1] for i in string] for string in strings]

	keskiarvo = [round(sum(i) / len(pituudet)) for i in zip(*pituudet)]
	
	dist = 0

	for string in pituudet:
		for a, b in zip(keskiarvo, string):
			dist += abs(a-b)

	print(dist)


for i in range(int(input())):
	print("Case #%i: " % (i+1), end="")
	case()	