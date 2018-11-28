import sys

def check_argv():
	if len(sys.argv) < 3:
		print("USAGE: #python lottery.py INPUT_FILE OUTPUT_FILE")
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
			a,b,k = map(int, input.readline().split())
			print a,b,k
			count = 0
			for i in range(a):
				for j in range(b):
					if i & j < k:
						count += 1
			print count
			ret += str(count) + "\n"
			output.write(ret)


"""
line =  "case #"+str(case_count)+": "+str(ret[0])+" "+str(ret[1])+"\n"
output.write(line)
"""

if __name__ == "__main__":
	main()