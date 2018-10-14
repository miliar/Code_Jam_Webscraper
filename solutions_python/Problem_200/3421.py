import sys

T = int(input().strip())

def is_tidy(s):
	s = ''.join(str(e) for e in s)
	#print(s)
	for i in range(0, len(s) -1):
		if int(s[i]) > int(s[i+1]):
			return False
	return True

for case in range(0, T):
	s = int(input().strip())
	_input = s
	s = list(str(s))
	while not is_tidy(s):
		for i in range(0, len(s)-1):
			if int(s[i]) > int(s[i+1]):
				s[i] = int(s[i]) - 1
				while i < len(s)-1:
					s[i+1] = 9
					i += 1
				break
		if int(s[0]) == 0:
			length = len(s) -1
			s = ''
			for i in range(0, length):
				s = s + '9'
	if type(i) is not str:
		s = ''.join(str(e) for e in s)
	#print("Case #" + str(case + 1) + ": " + str(s) + " --- " + str(_input))
	print("Case #" + str(case + 1) + ": " + str(s))

	
	
