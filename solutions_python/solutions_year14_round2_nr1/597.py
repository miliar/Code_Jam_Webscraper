

def main(fname='test.in', out_fname='test.out'):

	out_file = open(out_fname, 'w')

	def average(l):
		return sum(l)/len(l)


	def flatten(s):
		if len(s) <= 1:
			return s

		r = s[0]

		for c in s[1:]:
			if c != r[-1]:
				r += c

		return r

	def pop_dupes(l):
		counts = []
		strings = []

		for n, s in enumerate(l):
			if len(s) == 1:
				counts.append(1)
				strings.append('')
				continue

			for o, t in enumerate(s[1:]):
				if s[0] != t:
					counts.append(o+1)
					strings.append(s[o+1:])
					break
			else:
				counts.append(o+2)
				strings.append('')


		return counts, strings

	def f(l):
		moves = 0

		singles = [flatten(s) for s in l]

		for n, single in enumerate(singles[1:]):
			if singles[n] != single:
				return 'Fegla Won' 

		for char in singles[0]:
			#print l
			counts, l = pop_dupes(l)
			#print counts, l

			target = round(average(counts))
			moves += sum([abs(target - count) for count in counts])

		return int(moves)


	with open(fname, 'r') as in_file:
		rows = in_file.read().split('\n')
		cases = int(rows[0])

		string_count = None
		strings = []
		for row in rows[1:]:
			if not string_count:
				if strings:
					out_file.write('Case #{}: {}\n'.format(int(rows[0]) - cases, f(strings)))
					print f(strings)

				if not cases: 
					break

				cases -= 1
				string_count = int(row)
				strings = []
				continue

			strings.append(row)
			string_count -= 1

	out_file.close()

if __name__ == '__main__':
	#main()
	main('A-small-attempt1.in', 'A-small.out')

