# gcj stock functions

def readItems():
	line = raw_input();
	line = line.strip();
	line = line.split(" ");
	items = [];
	for item in line:
		try:
			if (item.find(".") >= 0):
				finalItem = float(item);
			else:
				finalItem = int(item);
		except ValueError:
			finalItem = item; # not an int or a float, must be a string.
		items.append(finalItem);
	return items;

def readString():
	line = raw_input();
	line = line.strip();
	return line;

testCases = readItems()[0];

for i in range(0,testCases):
	nm = readItems();
	duplicates = 0;
	for j in range(nm[0],nm[1]+1):
		s = str(j); # string-formatted version of i... needed for swapping digits
		foundPairs = set(); # found pairs for this #. Used to eliminate duplicates.
		for k in range(len(s)-1,0,-1):
			s2 = s[k:] + s[0:k];
			if (s2[0] != '0' and s2[0] >= s[0] and s != s2): # no leading 0's, no duplicates, first digit must be gte.
				j2 = int(s2);
				if (j2 >= j and j2 <= nm[1] and j2 not in foundPairs):
					duplicates += 1;
					foundPairs.add(j2);
	print "Case #"+str(i+1)+": "+str(duplicates);
