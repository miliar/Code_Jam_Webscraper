#input_lines = open("tmp.in").read().splitlines()
input_lines = open("A-small-attempt3.in").read().splitlines()
#input_lines = open("A-large-attempt0.in").read().splitlines()
#input_lines = open("B-small-attempt0.in").read().splitlines()
#input_lines = open("B-large-attempt0.in").read().splitlines()
#input_lines = open("C-small-attempt0.in").read().splitlines()
#input_lines = open("C-large-attempt0.in").read().splitlines()
#input_lines = open("D-small-attempt0.in").read().splitlines()
#input_lines = open("D-large-attempt0.in").read().splitlines()

test_num = int(input_lines[0])

for i in range(test_num):
	smax,s = input_lines[i+1].split()
	standing_people = int(s[0]) 
	invite_friend = 0
	for j in range(1,int(smax)+1):
		if standing_people >= j:
			standing_people += int(s[j])
		elif int(s[j]):
			invite_friend += j - standing_people
			standing_people += j+int(s[j]) 
	print "Case #" + str(i+1) + ": " + str(invite_friend)
