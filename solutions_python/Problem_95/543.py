import string

trans = string.maketrans('ynficwlbkuomxsevzpdrjgthaq', 'abcdefghijklmnopqrstuvwxyz')
print len(trans)
#string.translate(s, trans)

# _file = open("D:/Dropbox/Projects/CodeJAM/2012 Qualification Round/Problem_A/data.txt")
_file = open("D:/Dropbox/Projects/CodeJAM/2012 Qualification Round/Problem_A/A-small-attempt0.in")
lines = int(_file.readline())
_result = open("D:/Dropbox/Projects/CodeJAM/2012 Qualification Round/Problem_A/result.txt", "w")

line = _file.readline()
i = 1
while(line != ""):
	# text = line.translate(line, trans)
	line = line.replace("\n", "")
	if i > 1:
		_result.write("\n")
	_result.write("Case #" + str(i) + ": " + line.translate(trans))
	line = _file.readline()
	i += 1
	

_file.close()
_result.close()