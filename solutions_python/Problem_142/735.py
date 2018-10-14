import sys, operator
from itertools import groupby

def edit_distance(str1, str2):
	str1_short = ''.join([x[0] for x in groupby(str1)])
	str2_short = ''.join([x[0] for x in groupby(str2)])
	possibles = []
	if str1_short == str2_short:
		if str1 in str2 or str2 in str1:
			distance = abs(len(str1) - len(str2))
		else:
			count1 = 0
			count2 = 0
			distance = 0
			for letter in str1_short:
				while (count1 < len(str1) and count2 < len(str2) and str1[count1] == letter and str2[count2] == letter):
					count1 += 1
					count2 += 1
				while (count1 < len(str1) and str1[count1] == letter):
					count1 += 1
					distance += 1
				while (count2 < len(str2) and str2[count2] == letter):
					count2 += 1
					distance += 1
	else:
		distance = -1
	return distance
		
def dynamic(new, sofar):
	best_distance = []
	best_array = {}
	for val in sofar:
		distance, new_str = edit_distance(new, val) + sofar[val]
		if best_distance > distance:
			best_array = {}
			for cur in new_str:
				best_array[new_str] = distance
			best_distance = distance
		elif best_distance == [] or best_distance == distance:
			for cur in new_str:
				best_array[new_str] = distance

def main(argv):
	file_name = argv[0]
	f = open(file_name, 'r')
	number_tests = int(f.readline())

	for count in range(number_tests):
		first_line = int(f.readline())
		
		strings = [0] * first_line

		for i in range(first_line):
			#strings[i] = ''.join([x[0] for x in groupby(f.readline())])
			strings[i] = f.readline()
		if strings[0] == strings[1]:
			print "Case #" + str(count+1) + ": 0"
		else:
			distance = edit_distance(strings[0], strings[1])
			if distance >= 0:
				print "Case #" + str(count+1) + ": " + str(distance)
			else:
				print "Case #" + str(count+1) + ": Fegla Won"

if __name__ == "__main__":
   main(sys.argv[1:])
