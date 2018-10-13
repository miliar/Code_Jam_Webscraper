import sys
to_eng = 'yhesocvxduiglbkrztnwjpfmaq'
def trans(sentence):
	for a in range(len(sentence)-1):
		if sentence[a] == ' ':
			sys.stdout.write(' ')
		else:
			sys.stdout.write(to_eng[ord(sentence[a]) - ord('a')])
	sys.stdout.write("\n")

input = open(".\A-small-attempt0.in", "r")
num_of_cases = int(input.readline())
for i in range(1,num_of_cases+1):
	line = input.readline()
	print "Case #%d: " % (i),
	trans(line)
