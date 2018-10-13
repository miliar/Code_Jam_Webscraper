import string

# _file = open("D:/Dropbox/Projects/CodeJAM/2012 Qualification Round/Problem_B/data.txt")
_file = open("D:/Dropbox/Projects/CodeJAM/2012 Qualification Round/Problem_B/B-large.in")
lines = int(_file.readline())
_result = open("D:/Dropbox/Projects/CodeJAM/2012 Qualification Round/Problem_B/result.txt", "w")

line = _file.readline()
i = 1
while(line != ""):
	line = line.replace("\n", "")
	N, surp, min, googlers_all = line.split(" ", 3) # number of googlers, Surptising, min result, sums
	googlers = googlers_all.split(" ")
	
	surp, min = int(surp), int(min)
	
	# Count here
	max = 0
	for googler in googlers:
		googler = int(googler)
		# print googler
		if min*3-2 <= googler:
			max += 1
		elif min*3-4 <= googler and surp > 0 and min <= googler:
			max += 1
			surp -= 1
	# End counting
	
	if i > 1:
		_result.write("\n")
	_result.write("Case #" + str(i) + ": " + str(max))
	line = _file.readline()
	i += 1
	

_file.close()
_result.close()