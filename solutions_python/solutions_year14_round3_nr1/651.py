#!/usr/bin/python
import sys
import math

f = open(sys.argv[1], 'r')
inputs = f.read()
f2 = open("small_output", 'w')

lines = inputs.split('\n')
total_cases = lines[0]
for case in range(int(total_cases)):
	inputs = lines[case+1].split("/")
	num = int(inputs[0])
	den = int(inputs[1])
	unit = float(1)/pow(2,40)
	if num == 0 or float(num)/den/unit % 1 != 0:
		f2.write("Case #%i: impossible\n" % (case+1))
	else:
		den_pow = int(math.log(den, 2))
		num_pow = int(math.log(num, 2))
		f2.write("Case #%i: %i\n" % (case+1, den_pow-num_pow))