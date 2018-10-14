import sys

input = open(sys.argv[1], 'r')

t = int(input.readline())

for case in range(1, t + 1):

	line = input.readline()
	[s_max, audience] = line.split()
	s_max = int(s_max)
	audience = list(audience)
	audience = map(int, audience)

	invited = 0
	clapping = 0
	for i in range(s_max + 1):
		if (audience[i] > 0):
			if (clapping < i):
				invited += (i - clapping)
				clapping += invited
			clapping += audience[i]

	print('Case #' + str(case) + ': ' + str(invited))

input.close()
