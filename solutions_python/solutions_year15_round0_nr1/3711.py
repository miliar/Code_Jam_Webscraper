import sys

def solve(shynesses, verbose=0):
	
	people = [0]
	req = [0]
	added = [0]
	count = 1
	
	for s in shynesses:

		req.append( count-1)
		
		for k in range(s):
					
			if (req[count] <= people[-1]):
				people.append (people[-1]+1)
				added.append(0)
			else:
				added.append( req[count] - people[-1])				
				people.append (people[-1]+ 1 + added[-1])
				
			if (verbose):	
				print "People", people
				print "Required ",req
				print "Added", added
				print ""
				
		count = count + 1

	return sum(added)

def main():
	inputFile = "input1.txt"

	inFile = file(inputFile, 'r')
	numEntries = int(inFile.readline().strip())
	#print numEntries
	
	for i in range (numEntries):
		line = inFile.readline().strip()
		line = line.replace(" ","")

		s_max = int(line[0])
		s = []
		
		for j in range(1, len(line)):
			s.append(int(line[j]))
		
		#print s
		answer = solve(s)
		#print "=====\n"
		ansString = "Case #"+str((i+1))+": "+str(answer)
		print ansString
main()