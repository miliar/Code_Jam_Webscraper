#!/usr/bin/python

#============================================================

def quickSortList(list):
	if (len(list) <= 1):
		return list;

	point = list[0];

	[smallerList, largerList] = splitListByNum(point, list[1:]);
	smallerList = quickSortList(smallerList);
	largerList = quickSortList(largerList);

	return mergeList([smallerList, [point], largerList]);

#=============================================================

def splitListByNum(num, list):
	smallerList = [];
	largerList = [];

	for element in list:
		if (element <= num):
			smallerList[len(smallerList):] = [element];
		else:
			largerList[len(largerList):] = [element];

	return [smallerList, largerList];

#============================================================

def mergeList(lists):
	merged = [];
    
	for list in lists:
		for element in list:
			merged[len(merged):] = [element];

	return merged;

#=========================================================

if __name__ == '__main__':
	import sys, string
	infile = open('temp.txt', 'r');
	outfile = open('out.txt', 'w');

	lines = infile.readlines();

	infile.close();

        numTest = 0;
	i = 1;

	answer = 0;

############################################################
#loop thru testcase
############################################################
	while ((i < len(lines)) & (numTest < int(lines[0]))):
		inputs = [int(x.strip()) for x in lines[i].split()];
		
		level = inputs[0];
		keys = inputs[1];
		symbols = inputs[2];
		
		i = i + 1;

		freq = [int(x.strip()) for x in lines[i].split()];
		freq.sort();
		freq.reverse();
		#print(freq);

		if (symbols > (keys * level)):
			answer = "Impossible";
		else:
			j = 0;
			press = 1;
			totalpass = 0;
			ava = keys;

			while (j < len(freq)):		
				totalpass = totalpass + press * freq[j];
				#print (str(totalpass) + " ");
				
				ava = ava - 1;
				j = j + 1
				if (ava == 0):
					press = press + 1;
					ava = keys;
		
			answer = totalpass;	

                #######################################################
                #print to file selection
                #######################################################
		numTest = numTest + 1;
		outfile.write("Case #" + str(numTest) + ": ");
		outfile.write(str(answer));
		outfile.write("\n");

		i = i + 1;
                #######################################################		

		#try:
		#	input();
		#except:
		#	print("next");
#######################################################################

	outfile.close();
	print("DONE");