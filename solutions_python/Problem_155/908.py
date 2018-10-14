import math
def inputFromFile():
	filename = "A-small-attempt0.in"
	filepath = "/home/sayan/Downloads/"
	url = filepath + filename
	inp = []
	f = open(url, 'r')
	test_cases = int(f.readline()) 
	for dummy_num in range(test_cases):
		p = 0
		string = raw_input().split()
		smax = int(string[0])
		string = string[1]
		standing = 0
		for idx in range(len(string)):
				#print "standing, idx, p = " + str(standing) + " " + str(idx) + " " + str(p)
				if standing >= idx:
					standing += int(string[idx])
				else:
					p += idx - standing
					standing += idx - standing + int(string[idx])
				#print "standing, idx, p = " + str(standing) + " " + str(idx) + " " + str(p)
		inp.append(p)	
	return inp

def inputFromTerminal():
	inp = []
	test_cases = int(raw_input()) 
	#print "t = " + str(test_cases)
	for dummy_num in range(test_cases):
		p = 0
		string = raw_input().split()
		smax = int(string[0])
		string = string[1]
		standing = 0
		for idx in range(len(string)):
				#print "standing, idx, p = " + str(standing) + " " + str(idx) + " " + str(p)
				if standing >= idx:
					standing += int(string[idx])
				else:
					p += idx - standing
					standing += idx - standing + int(string[idx])
				#print "standing, idx, p = " + str(standing) + " " + str(idx) + " " + str(p)
		inp.append(p)
	return inp
	
def output(intsc):
	case = "Case #"
	oup = []
	for dummy_num in range(len(intsc)):
			oup.append(case + str(dummy_num + 1) + ": " + str(intsc[dummy_num]))
	return oup

def printToTerminal(oup):
	for string in oup:
		print string
		
def printToFile(oup):
	f = open('/home/sayan/Desktop/output.txt', 'w')
	for string in oup:
		f.write(string + '\n')
	
def decr(num):
	return num - 1 
					
printToTerminal(output(inputFromTerminal()))
#printToFile(output(inputFromFile()))
