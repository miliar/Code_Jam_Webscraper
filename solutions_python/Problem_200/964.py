# Google Code Jam practice problems

#file_in = "test.txt"
#file_in = "B-small-attempt0.in"
file_in = "B-large.in"

file_out = "output.txt"

def answer(N):
	
	N = str(N)
	flag = False
	while flag == False:
		if is_tidy(N):
			if N.startswith("0"):
				N = N[1:]
			return N
		flag = True
		for i in range(len(N)-1):
			if int(N[i]) > int(N[i+1]):
				flag = False
				new_num = N[:i]
				
				new_num += str(int(N[i]) - 1)
				while len(new_num) < len(N):
					new_num += "9"
				N = new_num
				#print(N)
	
	
			
def is_tidy(num):
	num = str(num)
	for i in range(1, len(num)):
		if int(num[i]) < int(num[i-1]):
			return False
	return True
	
	
def write_file():
	f = open(file_in)
	out = open(file_out, "w")
	num_cases = int(f.readline())
	for i in range(num_cases):
		test_case = int(f.readline().strip())
		output = answer(test_case)
		out.write("Case #" + str(i+1) + ": " + str(output) + "\n")
		print("Case #" + str(i+1) + ": " + str(output))
	f.close()
	out.close()
	
write_file()