import math

def IsWhole(x):
	return x == math.floor(x) 

def ispalindrome(zahl):
	string = str(zahl)
	if string == string[::-1]:
		print string,zahl,string[::-1]
		return 1
	return 0

def isfair(zahl):
	if not ispalindrome(zahl):
		return 0
	temp = math.sqrt(zahl)
	if IsWhole(temp):
		if ispalindrome(int(temp)):
			print temp,zahl,'jo'
			return 1
	return 0

def anzahl_fair(von, bis):
	anzahl = 0
	o.write(str(int(math.sqrt(von)))+'\n')
	for i in range(int(math.sqrt(von)),bis+1):
		if isfair(i):
			if i >= von:
				anzahl += 1
	return anzahl

i = open("input.txt","r")
o = open("output.txt", "w")
cases = int(i.readline())
print cases
for case in range(cases):
	case_number = case + 1
	line = i.readline()
	case_array = line.strip().split(' ')
	print case_array
	s = 'Case #' + str(case_number)+ ': ' + str(anzahl_fair(int(case_array[0]), int(case_array[1])))
	o.write(s+'\n')
o.close()
i.close()