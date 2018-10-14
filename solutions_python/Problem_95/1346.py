import sys

input  = ["y", 
		  "e",
		  "q",
		  "z",
		  "ejp mysljylc kd kxveddknmc re jsicpdrysi",
		  "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
		  "de kr kd eoya kw aej tysr re ujdr lkgc jv"]

output = ["a",
		  "o",
		  "z",
		  "q",
		  "our language is impossible to understand",
		  "there are twenty six factorial possibilities",
		  "so it is okay if you want to just give up"]

dict = {}

for j in range(len(input)):
	for i in range(len(input[j])):
		inp = input[j][i]
		out = output[j][i]
		if inp != ' ':
			if inp in dict.keys():
				if out != dict[inp]:
					print("error in %d out %d", {inp, out}) 
			else:
				dict[inp] = out

#for a, b in sorted(dict.items()):
#	print a, b

t = raw_input()

for i in range(int(t)):
	s = raw_input()
	sys.stdout.write("Case #%d: " % (i + 1)) 
	for j in range(len(s)):
		if s[j] == ' ':
			sys.stdout.write(s[j])		
		else:
			sys.stdout.write(dict[s[j]])
	print ""		

