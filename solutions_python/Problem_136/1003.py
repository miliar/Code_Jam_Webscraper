import sys
input_file = open(sys.argv[1], 'r')
output_file = open(sys.argv[2], 'w')

cases = int(input_file.readline().strip())
for case in range(cases):
	c, f, x = map(float, input_file.readline().strip().split())
	k = int(x / c - 2.0 / f)
	t = 0
	if k > 0:
		for i in range(k):
			t += c / (2 + i * f)
		t += x / (2 + k * f)
	else:
		t = x / 2
	output_file.write('Case #%d: %.7f\n' % (case + 1, t))
input_file.close()
output_file.close()

