def solve(str):
	indx_1 = int(str.pop(0)) - 1
	cand_1 = str[indx_1].split(" ")
	del str[0:4]
	indx_2 = int(str.pop(0)) - 1
	cand_2 = str[indx_2].split(" ")
	
	lst = filter(lambda v: v in cand_1, cand_2)
	#print("\n"+",\t".join(cand_1))
	#print(",\t".join(cand_2) + "\t\t =>"+",".join(lst))
	if len(lst) == 1: 
		#print lst[0]
		return lst[0]
	if len(lst) > 1: 
		#print "Bad magician!"
		return "Bad magician!"
	if len(lst) == 0: 
		#print "Volunteer cheated!"
		return "Volunteer cheated!"
	
with open('A-small-attempt2.in') as f:
    input = f.read().splitlines()
numCases = input.pop(0)

f = open('A-small.out', 'w')
for i in range(0,int(numCases)):
	f.write("Case #" + str(i+1) + ": " + solve(input[i*10:i*10+10])+"\n")