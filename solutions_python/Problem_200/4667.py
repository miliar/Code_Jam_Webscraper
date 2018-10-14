input_file = open("input.txt" , "r")
output_file = open("output.txt" , "w")

single_int = []
flag = 1

no_test = int(input_file.readline())

for i in range(no_test):
	test_num = int(input_file.readline())
	single_int = [int(num) for num in str(test_num)]
	while(1):
		flag = 1
		for k in range(len(single_int) - 1):
			j = k + 1
			if(single_int[k] > single_int[j]):
				flag = 0
				break
		if(flag == 1):
			output_file.write("Case #" + str(i + 1) + ": " + str(test_num) + "\n")
			break
		test_num = test_num - 1
		single_int = [int(num) for num in str(test_num)]

input_file.close()
output_file.close()
