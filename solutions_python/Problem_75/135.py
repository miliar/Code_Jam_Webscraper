T = int(raw_input())

for tc in range(0, T):
	input = raw_input().split(' ')
	invoke = input[-1]
	
	s = ""
	for x in invoke:
		s += x
		
		for t in input[1:int(input[0])+1]:
			if s[-2:] == t[:2] or s[-2:] == t[-2::-1]:
				s = s[:-2] + t[2]
		
		for t in input[int(input[0])+2:-2]:
			if t[0] in s and t[1] in s:
				s = ""
	
	print "Case #" + str(tc+1) + ": " + str(list(s)).replace("'","")
