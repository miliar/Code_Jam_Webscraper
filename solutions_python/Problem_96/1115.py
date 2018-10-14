input = open("input.txt", "r")
output = open("output2.txt","w")
testcases = int(input.readline())
count = 1
while count <= testcases:
	in_line = input.readline()
	data = in_line.split(" ")
	special_cases = int(data[1])
	max_score = int(data[2])
	total = 0
	for index in range(3,len(data)):
		score = int(data[index])
		if score < max_score:
			continue
		div = score/3
		mod = score%3
		if div >= max_score:
			total = total+1
		elif div == max_score-1:
			if mod >= 1:
				total = total+1
			elif special_cases>0:
				total = total+1
				special_cases = special_cases - 1
		elif div == max_score-2 and mod == 2 and special_cases>0 :
			total = total+1
			special_cases = special_cases - 1
	out_line = "Case #"+repr(count)+": "+repr(total)
	output.write(out_line+"\n")
	count = count +1