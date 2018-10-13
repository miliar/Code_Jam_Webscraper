import math

def isTidy(number):
    for i in range(1, len(number)):
        if number[i] < number[i-1]:
            return False
    return True

def find(number):
    if number == "0":
        return ""
    if(isTidy(number)):
        return number
    l = len(number)
    i = 1
    while i < len(number):
        if number[i] >= number[i - 1]:
            i += 1
        else:
            break
    prefix = number[:i - 1] + str(int(number[i - 1]) - 1)
    result = find(prefix)
    for j in range(i, l):
        result += '9'
    return result

inputfilename = "B-large.in"
fin = open(inputfilename, "r")
outputfilename = "tidy_numbers_output.txt"
fout = open(outputfilename, "w")
t = fin.readline()
t = int(t)
for i in xrange(1, t+1):
	line = fin.readline().split(" ")
	s = line[0].strip()
	result = "Case #" + str(i) + ": " + find(s) + '\n'
	fout.write(result)
fin.close()
fout.close()
