#!/usr/bin/env python

from __future__ import print_function

import sys

with open(sys.argv[1]) as input_file:
	input_file.readline()
	for case, audience in enumerate(input_file, 1):
		standing = 0
		guests = 0
		for shyness, people in enumerate(map(int, audience.split()[1])):
			if shyness > standing:
				new_guests = shyness - standing
				guests += new_guests
				standing += new_guests
			standing += people
		print('Case #%s: %s' % (case, guests))

