#!/usr/bin/python

f = open("input.txt", "r")

o = open("output.txt", "w")

line_count = int(f.readline())

case = 0

for line in range(line_count):
	case += 1
	answer = 0
	case_split = f.readline().strip().split(" ")
	audience = case_split[1]
	shyness_level = int(case_split[0]) + 1
	current_ppl = 0
	for level in range(shyness_level):
		shy_audi_cnt = int(audience[level])
			
		if (current_ppl >= level ):
			current_ppl += shy_audi_cnt
			continue
		else:
			answer += (level - current_ppl)
			current_ppl += (level - current_ppl)
		
		current_ppl += shy_audi_cnt

	o.write("Case #" + str(case) + ": " + str(answer) + "\n")
	
