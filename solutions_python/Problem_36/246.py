#############################################
def lookfortext(find, completeString):
	indexes = []
	total = 0
	for i in range(len(completeString)):
		if completeString[i] is find[0]:
			indexes.append(i)
	
	if len(indexes) is 0:
		return 0
	elif len(find) is 1:
		return len(indexes) 
	else:
		for index in indexes:
			total += lookfortext(find[1:],completeString[index+1:])
		return total
		
	
#############################################

file = open("C-small.in", "r")
output = open("output.txt", "w");

case_n = 1
for case in file.readlines()[1:]:
	output.write("Case #%d: %04d\n" % (case_n, lookfortext("welcome to code jam", case)))
	case_n += 1
output.close()
file.close()
