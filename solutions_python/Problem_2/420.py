#!/usr/bin/python

import sys

if len(sys.argv) <= 1:
	print "Please provide an input file"
	sys.exit(1)

# data input
input_file_name = sys.argv[1]
input_file = file(input_file_name, "r")
output_file = file("output.txt", "w")

test_case_count = int(input_file.readline())
test_cases = []

for i in range(test_case_count):
	turnaround_time = int(input_file.readline())
	tmp = input_file.readline().split(" ")
	ab_count, ba_count = int(tmp[0]), int(tmp[1])
	
	trips = []
	for j in range(ab_count + ba_count):
		modifier = "ba" if j >= ab_count else "ab"
		tmp = input_file.readline().split(" ")
		trips.append((int(tmp[0].split(":")[0]) * 60 + int(tmp[0].split(":")[1]), 
			         int(tmp[1].split(":")[0]) * 60 + int(tmp[1].split(":")[1]), 
					 modifier))

	trips.sort()
	
	trains_at_a = 0
	trains_at_b = 0
	trains_from_a = 0
	trains_from_b = 0
	
	for t in range(24 * 60):
		for trip in trips:
			if trip[1] + turnaround_time == t:
				if trip[2] == "ba":
					trains_at_a = trains_at_a + 1
				if trip[2] == "ab":
					trains_at_b = trains_at_b + 1

			if trip[0] == t:
				if trip[2] == "ab":
					if trains_at_a > 0: 
						trains_at_a = trains_at_a - 1
					else:
						trains_from_a = trains_from_a + 1
				if trip[2] == "ba":
					if trains_at_b > 0: 
						trains_at_b = trains_at_b - 1
					else:
						trains_from_b = trains_from_b + 1
	
	output_file.write("Case #%s: %s %s\n" % (i + 1, trains_from_a, trains_from_b))
		
output_file.close()
input_file.close()