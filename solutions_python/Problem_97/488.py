import string

# _file = open("D:/Dropbox/Projects/CodeJAM/2012 Qualification Round/Problem_C/data.txt")
_file = open("D:/Dropbox/Projects/CodeJAM/2012 Qualification Round/Problem_C/C-large.in")
lines = int(_file.readline())
_result = open("D:/Dropbox/Projects/CodeJAM/2012 Qualification Round/Problem_C/result.txt", "w")

line = _file.readline()
l = 1
while(line != ""):
	line = line.replace("\n", "")
	min, max = line.split(" ")
	min, max = int(min), int(max)
	
	# Count here
	sum = 0
	size = len(str(min))
	for i in range(min, max+1):
		tuples = []
		for j in range(1, size):
			i_str = str(i)
			i_str_rec = i_str[j:]+i_str[:j]
			i_rec = int(i_str_rec)
			if i_rec > i and i_rec <= max:
				i_join = int(i_str + i_str_rec)
				if(not i_join in tuples):
					sum += 1
					tuples.append(i_join)
				# else:
					# print i_str
				
	# End counting
	
	if l > 1:
		_result.write("\n")
	_result.write("Case #" + str(l) + ": " + str(sum))
	line = _file.readline()
	l += 1
	

_file.close()
_result.close()