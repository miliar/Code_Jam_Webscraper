import sys

# Since the file structure is 100% ensured, just skip the line count
sys.stdin.readline()

for i, line in enumerate(sys.stdin):
	[maxShyness, people] = line.split(' ')

	extra = 0
	count = 0

	for shiness, num in enumerate(people.strip()):
		num = int(num)

		needed = shiness - count

		# If friends are needed, bring them in.
		if needed > 0:
			extra += needed
			count += needed

		count += num

	print "Case #%d: %d" % (i + 1, extra)