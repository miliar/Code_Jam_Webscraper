from itertools import islice
import sys

if __name__=="__main__":
	num_tests = None
	test_sample = 0
	with open("A-small-attempt0.in", 'r') as infile:
		if not num_tests:
			num_tests = int(infile.readline())
		for test_sample in range(0,num_tests):
				lines_iter = islice(infile, 10)
				lines = []
				for line in lines_iter:
					lines.append(line)
				row1 = int(lines[0])
				row2 = int(lines[5])
				set1 = set(map(int,lines[row1].split(' ')))
				set2 = set(map(int,lines[5+row2].split(' ')))
				inter = set1.intersection(set2)
				if len(inter) == 1:
					print "Case #"+str(test_sample+1)+": "+str(inter.pop())
				elif len(inter) > 1:
					print "Case #"+str(test_sample+1)+": Bad magician!"
				else:
					print "Case #"+str(test_sample+1)+": Volunteer cheated!"	
				test_sample += 1
					
