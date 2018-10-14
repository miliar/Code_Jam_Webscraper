'''
prima donna
shyness level, Si - atleast Si audience member have already stood up to clap

?? Minimum number of friends needed to guarantee a standing ovation

T, test cases
Each case has a single line



'''

import fileinput
import sys


def main():
	T = 0; # test case
	tIndex = -1; # test case index
	for line in sys.stdin:
		tIndex = tIndex + 1;
		# First line, reports number of test case
		if tIndex == 0:
			T = int(line);
		else:
			# Rest of the lines have test cases in them
			splitStr = line.split();
			shynessMax = int(splitStr[0]);
			shynessStr = splitStr[1];

			minFriend = 0
			tempCount = 0
			index = -1
			for c in shynessStr:
				index = index + 1;
				audAtC = int(c);
				tempCount = tempCount + audAtC;

				if (tempCount < index + 1):
					tempCount = tempCount + 1;
					minFriend = minFriend + 1;

			print "Case #%d: %d" % (tIndex, minFriend);


if __name__ == "__main__":
    main()


