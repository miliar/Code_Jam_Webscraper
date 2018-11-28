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

for x in range(test_case_count):
	search_machine_count = int(input_file.readline())

	search_engines = []
	for y in range(search_machine_count):
		search_engines.append(input_file.readline().strip())

	search_string_count = int(input_file.readline())
	search_strings = []
	for y in range(search_string_count):
		search_strings.append(input_file.readline().strip())
		
	counter = 0
	possible_search_engines = search_engines[:]
	for search_string in search_strings:
		if search_string in possible_search_engines:
			possible_search_engines.remove(search_string)
		if len(possible_search_engines) == 0:
			counter = counter + 1
			possible_search_engines = search_engines[:]
			possible_search_engines.remove(search_string)
	
	output_file.write("Case #%s: %s\n" % (x + 1, counter))

input_file.close()
output_file.close()

