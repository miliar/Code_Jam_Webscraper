input = open("A-small-attempt2.in","r")
output = open("A-small-attempt2.out","w")
eng = "yhesocvxduiglbkrztnwjpfmaq"
test_cases = int(input.readline())
for test in range(test_cases):
	new_string = ""
	line = input.readline()
	for c in line:
		if c.isalpha():
			new_string += eng[ord(c)-97]
		else:
			new_string += c
	output.write("Case #%i: %s"%(test+1,new_string))