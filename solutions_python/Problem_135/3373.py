# Nadeem Malik

import sys

with open(sys.argv[1]) as f:
    content = f.readlines()

f = open(sys.argv[2], 'w')

num_tests = int(content[0]);

if(num_tests >= 1 and num_tests <= 100):
	line_idx = 1;
	tests_done = 1;
	while(tests_done <= num_tests):
		answ1 = int(content[line_idx]);
		answ2 = int(content[line_idx + 5]);

		if((answ1 >= 1 and answ1 <= 4) and (answ2 >=1 and answ2 <= 4)): 

			arr1 = [None] * 4;
			arr1[0] = list(content[line_idx+1].rstrip().split(" "));
			arr1[1] = list(content[line_idx+2].rstrip().split(" "));
			arr1[2] = list(content[line_idx+3].rstrip().split(" "));
			arr1[3] = list(content[line_idx+4].rstrip().split(" "));

			arr2 = [None] * 4;
			arr2[0] = list(content[line_idx+6].rstrip().split(" "));
			arr2[1] = list(content[line_idx+7].rstrip().split(" "));
			arr2[2] = list(content[line_idx+8].rstrip().split(" "));
			arr2[3] = list(content[line_idx+9].rstrip().split(" "));


			#print("answ1 was " + answ1);
			#print("arr1 was " + str(arr1));

			#print("answ2 was " + answ2);
			#print("arr2 was " + str(arr2));

			# get the row with the card for each arrangement
			answ1_row = arr1[answ1 - 1];
			answ2_row = arr2[answ2 - 1];

			cards_in_common = set(answ1_row).intersection(set(answ2_row));

			if(len(cards_in_common) == 0):
				f.write("Case #" + str(tests_done) + ": Volunteer cheated!\n");
			elif(len(cards_in_common) == 1):
				f.write("Case #" + str(tests_done) + ": " + str(cards_in_common.pop()) + "\n");
			else:
				f.write("Case #" + str(tests_done) + ": Bad magician!\n");
		else:
			print("Case #3: Volunteer cheated!\n");


		line_idx += 10;
		tests_done += 1;
