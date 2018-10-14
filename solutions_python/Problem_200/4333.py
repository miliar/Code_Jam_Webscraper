file = open("B-small-attempt2.in")
output = open("outputfile1", "w")
case_count = 1
if_found = False
file.readline()
for line in file:
# 	first digits
# 	number of digits
	num = int(line)
	print("num ", num)
	while num >= 0:
		line_c = str(num)
# 		print(num)
		for i in range(len(line_c)-2, -1, -1):
# 			print(i, line[i], i+1, line[i+1])
			if int(line_c[i]) > int(line_c[i+1]):
				if_found = True
# 				print("fdsf")
				break
		if not if_found:
			print("Case #"+str(case_count)+": "+line_c)
			output.write("Case #"+str(case_count)+": "+line_c+"\n")
			break
		else:
			if_found = False
		num -= 1
	case_count += 1
# 	if case_count>10:
# 		break
print("hello world")