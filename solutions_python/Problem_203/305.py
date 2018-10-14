


def fill(cake, R, C):

	for row in cake:
		if filter(lambda x : x!='?', row):
			first = True
			letter = '?'
			for j in xrange(C):
				if row[j] == '?' and not first:
					row[j] = letter
				elif row[j] != '?':
					letter = row[j]
					if first:
						first = False
						for k in xrange(j):
							row[k] = letter

	first = True
	row_to_copy = ['?']*C
	for i in xrange(R):
		if cake[i][0] == '?' and not first:
			for j in xrange(C):
				cake[i][j] = row_to_copy[j]
		elif cake[i][0] != '?':
			row_to_copy = cake[i]
			if first:
				first = False
				for k in xrange(i):
					for j in xrange(C):
						cake[k][j] = row_to_copy[j]

	return cake

	



def main():
	T = int(raw_input())

	for t in xrange(T):

		line = raw_input().split()
		R, C = int(line[0]), int(line[1])

		cake = [list(raw_input()) for r in xrange(R)]

		print 'Case #'+str(t+1)+':'
		print '\n'.join(map(''.join, fill(cake, R, C)))


main()