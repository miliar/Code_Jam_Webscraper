mapping = {' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z':'q','q':'z'};

# gcj stock functions

def readItems(fp):
	line = fp.readline();
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

def readString(fp):
	line = fp.readline();
	line = line.strip();
	return line;

def translate(string):
	final = "";
	for c in string:
		if (mapping.has_key(c)):
			final += mapping[c];
		else:
			final += c;
	return final;

fp = open("gcjinput.txt","r");

line1 = readItems(fp);
lines = line1[0];

for i in range(0,lines):
	line = readString(fp);
	print "Case #"+str(i+1)+": "+translate(line);
fp.close();
