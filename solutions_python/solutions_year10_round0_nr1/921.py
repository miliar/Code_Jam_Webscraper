import sys
import math

def execute(n, k):
	if math.pow(2, n) - 1 > k:
		return "OFF"

	while k > 0 and math.pow(2, n) < k:
		k -= math.pow(2, n)
	if k == math.pow(2, n) - 1:
		return "ON"
	return "OFF"

if len(sys.argv) < 2:
	quit('Too few arguments.')

count = 0
T = 0
for line in file(sys.argv[1]):
	line = line.strip()
	count += 1
	if count == 1:
		T = int(line)
		continue

	if len(line) == 0:
		# make sure we don't process something empty
		continue

	N, K = line.split()
	print "Case #%s: %s" % (count - 1, execute(int(N), float(K)))
