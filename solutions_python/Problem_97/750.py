from sets import Set
sourceFile = "large.in";
outputFile = "large.out";

s_handler = open(sourceFile, 'r');
o_handler = open(outputFile, 'w');

T = s_handler.readline();

checkbag = Set();

for i in range(1, int(T)+1):
	line = s_handler.readline().strip();
	theRange = line.split(" ");
	A = theRange[0];
	B = theRange[1];
	str_len = len(A);
	A_num = int(A);
	B_num = int(B);
	total = 0;
	for num in range(A_num, B_num):
		checkbag.clear();
		str_num = str(num);
		for separator in range(1, str_len):
			if (str_num[separator] < str_num[0])
				continue;
			new_str = str_num[separator:] + str_num[:separator];
			new_num = int(new_str);
			if (new_num in checkbag):
				continue;
			checkbag.add(new_num);
			if (num < new_num) and (new_num <= B_num):
				total+=1;
	print total;
	o_handler.write("Case #" + str(i) + ": " + str(total) + "\n");

s_handler.close();
o_handler.close();
