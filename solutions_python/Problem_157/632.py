def inputFromFile():
	filename = "C-small-attempt6.in"
	filepath = "/home/sayan/Downloads/"
	url = filepath + filename
	inp = []
	f = open(url, 'r')
	dic = {
				'1': {'1': '1', 'i': 'i', 'j': 'j', 'k': 'k'},
				'i': {'1': 'i', 'i': '-1', 'j': 'k', 'k': '-j'},
				'j': {'1': 'j', 'i': '-k', 'j': '-1', 'k': 'i'},
				'k': {'1': 'k', 'i': 'j', 'j': '-i', 'k': '-1'},				
	}
	test_cases = int(f.readline())
	#print test_cases
	for dummy_num in range(test_cases):
	
		l, x = map(int, f.readline().split())
		print l, x
		s = f.readline().rstrip()
		print s
		if l * x < 3 or l < 2:
			inp.append(0)
		else:
			string = s * x
			
			while string[0] != 'i' and len(string) > 3:
			
				if string[0] != '-':
					first = string[0]
					second = string[1]
					print first, second
					rp = dic[first][second]
					if len(string) > 2:
						string = rp + string[2:]
					else:
						string = rp
				else:
					first = string[1]
					second = string[2]
					print first, second
					rp = dic[first][second]
					if len(rp) > 1:
						if len(string) > 3:
							string = rp[1:] + string[3:]
						else:
							string = rp[1:]
					else:
						if len(string) > 3:
							string = '-' + rp + string[3:]
						else:
							string = '-' + rp
						
			while string[:2] != 'ij' and len(string) > 3:
			
				if string[1] != '-':
					first = string[1]
					second = string[2]
					rp = dic[first][second]
					if len(string) > 3:
						string = string[0] + rp + string[3:]
					else:
						string = string[0] + rp
				else:
					first = string[2]
					second = string[3]
					rp = dic[first][second]
					if len(rp) > 1:
						if len(string) > 4:
							string = string[0] + rp[1:] + string[4:]
						else:
							string = string[0] + rp[1:]
					else:
						if len(string) > 4:
							string = string[0] + '-' + rp + string[4:]
						else:
							string = string[0] + '-' + rp
						
						
			while len(string) > 3:
				print len(string)
				if string[2] != '-':
					first = string[2]
					second = string[3]
					print first, second
					rp = dic[first][second]
					if len(string) > 4:
						string = string[:2] + rp + string[4:]
					else:
						string = string[:2] + rp
				else:
					first = string[3]
					if len(string) > 4:
						second = string[4]
					else:
						break
					rp = dic[first][second]
					if len(rp) > 1:
						if len(string) > 5:
							string = string[:2] + rp[1:] + string[5:]
						else:
							string = string[:2] + rp[1:]
					else:
						if len(string) > 5:
							string = string[:2] + '-' + rp + string[5:]
						else:
							string = string[:2] + '-' + rp
			#print string
			if string == 'ijk' and len(string) == 3:
				inp.append(1)
			else:
				inp.append(0)
	return inp

def inputFromTerminal():
	inp = []
	
	dic = {
				'1': {'1': '1', 'i': 'i', 'j': 'j', 'k': 'k'},
				'i': {'1': 'i', 'i': '-1', 'j': 'k', 'k': '-j'},
				'j': {'1': 'j', 'i': '-k', 'j': '-1', 'k': 'i'},
				'k': {'1': 'k', 'i': 'j', 'j': '-i', 'k': '-1'},				
	}
	test_cases = int(raw_input())
	
	for dummy_num in range(test_cases):
	
		l, x = map(int, raw_input().split())
		s = raw_input()
		if l * x < 3 or l < 2:
			inp.append(0)
		else:
			string = s * x
			#print string
			
			while string[0] != 'i' and len(string) > 3:
			
				if string[0] != '-':
					first = string[0]
					second = string[1]
					rp = dic[first][second]
					if len(string) > 2:
						string = rp + string[2:]
					else:
						string = rp
				else:
					first = string[1]
					second = string[2]
					rp = dic[first][second]
					if len(rp) > 1:
						if len(string) > 3:
							string = rp[1:] + string[3:]
						else:
							string = rp[1:]
					else:
						if len(string) > 3:
							string = '-' + rp + string[3:]
						else:
							string = '-' + rp
						
			while string[:2] != 'ij' and len(string) > 3:
			
				if string[1] != '-':
					first = string[1]
					second = string[2]
					rp = dic[first][second]
					if len(string) > 3:
						string = string[0] + rp + string[3:]
					else:
						string = string[0] + rp
				else:
					first = string[2]
					second = string[3]
					rp = dic[first][second]
					if len(rp) > 1:
						if len(string) > 4:
							string = string[0] + rp[1:] + string[4:]
						else:
							string = string[0] + rp[1:]
					else:
						if len(string) > 4:
							string = string[0] + '-' + rp + string[4:]
						else:
							string = string[0] + '-' + rp
						
						
			while len(string) > 3:
			
				if string[2] != '-':
					first = string[2]
					second = string[3]
					rp = dic[first][second]
					if len(string) > 4:
						string = string[:2] + rp + string[4:]
					else:
						string = string[:2] + rp
				else:
					first = string[3]
					if len(string) > 4:
						second = string[4]
					else:
						break
					rp = dic[first][second]
					if len(rp) > 1:
						if len(string) > 5:
							string = string[:2] + rp[1:] + string[5:]
						else:
							string = string[:2] + rp[1:]
					else:
						if len(string) > 5:
							string = string[:2] + '-' + rp + string[5:]
						else:
							string = string[:2] + '-' + rp
			print string
			if string == 'ijk' and len(string) == 3:
				inp.append(1)
			else:
				inp.append(0)
	return inp
	
def output(intsc):
	case = "Case #"
	yes = "YES"
	no = "NO"
	oup = []
	for dummy_num in range(len(intsc)):
		if intsc[dummy_num]:
			oup.append(case + str(dummy_num + 1) + ": " + yes)
		else:
			oup.append(case + str(dummy_num + 1) + ": " + no)
	return oup

def printToTerminal(oup):
	for string in oup:
		print string
		
def printToFile(oup):
	f = open('/home/sayan/Desktop/output.txt', 'w')
	for string in oup:
		f.write(string + '\n')
		
printToFile(output(inputFromFile()))
#printToTerminal(output(inputFromTerminal()))
