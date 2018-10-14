import sys

def check_argv():
	if len(sys.argv) < 3:
		print("USAGE: #python repeater.py INPUT_FILE OUTPUT_FILE")
		sys.exit()

def main():
	input_file = sys.argv[1]
	output_file = sys.argv[2]
	print input_file
	print output_file
	with open(input_file, "rb") as input, open(output_file,"w") as output:
		case_count = int(input.readline())
		for case_idx in range(1, case_count+1):
			ret = "Case #"+str(case_idx)+": "
			# par1,par2,... = map(int, input.readline().split())
			# input string: input.readline().rstrip().split("/")[1:0]
			n = int(input.readline())
			lines = []
			for i in range(n):
				lines.append(input.readline().strip())
			print lines
			new_lines = []
			new_lines_count_list = []
			for line in lines:
				string = ""
				str_tmp = ""
				count = 0
				new_lines_count = []
				for char in line:
					if char != str_tmp:
						string += char
						if str_tmp != "":
							new_lines_count.append(count)
						count = 0
					str_tmp = char
					count += 1
				new_lines_count.append(count)
				new_lines_count_list.append(new_lines_count)
				new_lines.append(string)
			print new_lines
			print new_lines_count_list
			# check possibility
			possible = True
			ptn_tmp = new_lines[0]
			for ptn in new_lines:
				if ptn != ptn_tmp:
					possible = False
					break
				ptn_tmp = ptn
			print possible
			if possible:
				diff = 0
				for i in range(len(new_lines_count_list[0])):
					avg_tmp = 0
					for j in range(n):
						avg_tmp += new_lines_count_list[j][i]
					avg_tmp = avg_tmp/n
					for j in range(n):
						if new_lines_count_list[j][i] >= avg_tmp:
							diff += new_lines_count_list[j][i] - avg_tmp
						else:
							diff += avg_tmp - new_lines_count_list[j][i]
				ret += str(diff) + "\n"
			else:
				ret += "Fegla Won\n"
			output.write(ret)


"""
line =  "case #"+str(case_count)+": "+str(ret[0])+" "+str(ret[1])+"\n"
output.write(line)
"""

if __name__ == "__main__":
	main()