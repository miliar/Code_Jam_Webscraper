import collections
compare = lambda x, y: collections.Counter(x) == collections.Counter(y)

file_in = open("A.in", "r")
file_out = open("A-small.out", "w")

def output (string):
	file_out.write(string + "\n")
	print(string)

case = 1
read = 0
sigs = []
conts = []
strings = []
for number, line in enumerate(list(file_in)):
	if number == 0:
		continue
	if read == 0:
		read = int(line[:-1])
	else:
		strings.append(line[:-1])
		read -= 1
	if read == 0:
		valid = True
		m = 0
		for s in strings:
			sig = []
			cont = []
			for char in s:
				if len(sig) == 0 or sig[-1] != char:
					sig.append(char)
					cont.append(1)
				elif len(sig) != 0:
					cont[len(cont) - 1] += 1
			if len(cont) > m:
				m = len(cont)
			sigs.append(sig)
			conts.append(cont)
		for sig in sigs[1:]:
			if not compare(sig, sigs[0]):
				valid = False
		if valid:
			mxt = 0
			for i in range(m):
				mn = 10000
				mx = 1
				for cont in conts:
					if cont[i] < mn:
						mn = cont[i]
					if cont[i] > mx:
						mx = cont[i]
				mxt += mx - mn
		if not valid:
			output("Case #{}: ".format(case) + "Fegla Won")
		else:
			output("Case #{}: ".format(case) + str(mxt))
		sigs = []
		strings = []
		conts = []
		case += 1

file_in.close()
file_out.close()