import sys

file = open(sys.argv[1],"r")
output = ""
input = file.readlines()
file.close()
# print input
caseNo = 1
# caseNo = int(input[0])
input = input[1:]


while len(input) > 0:
	N = input.pop(0)
	list = input.pop(0)
	
	list = list.split(" ")
	list = [int(x) for x in list]
	sortedlist = sorted(list)
	
	total = 0
	for x in range(0,len(list)):
		if list[x] != sortedlist[x]:
			total += 1

	output = output + "Case #" + str(caseNo) + ": " + str(total) + "\n"
	caseNo +=1

file = open(sys.argv[2],"w")
file.write(output)
file.close