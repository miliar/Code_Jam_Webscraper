#	Project:	Google Code Jam
#	Problem:	File Fix-it
#	File:		filefixit.py
#	Date:		22 May 2010
#	Author:		Christopher Busby

input = "A-large.in"
output = input.replace(".in", ".out")

fileInput = open(input, "r")
fileOutput = open(output, "w+")

def navigate(files, dirs, index, count):
	if(index >= len(dirs)):
		return count
	dir = dirs[index]
	if(dir not in files):
		count += 1
		files[dir] = {}
	files = files[dir]
	return navigate(files, dirs, index + 1, count)
	

testCases = int(fileInput.readline())

for i in range(0, testCases):
	root = {}
	info = fileInput.readline().split(" ")
	for j in range(0, len(info)):
		info[j] = int(info[j])
	
	for j in range(0, info[0]):
		dirs = fileInput.readline().strip().split("/")
		navigate(root, dirs, 1, 0)
	
	count = 0
	for j in range(0, info[1]):
		dirs = fileInput.readline().strip().split("/")
		count += navigate(root, dirs, 1, 0)
	
	fileOutput.write("Case #" + str(i + 1) + ": " + str(count) + "\n")

fileOutput.close()
fileInput.close()