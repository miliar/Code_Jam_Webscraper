import sys

this_prog = sys.argv[:1][0]
in_args   = sys.argv[1:]
in_count  = len(in_args)

target_input = in_args[0]

f = open(target_input,'r')
data = f.read()
input = []
for d in data.split("\n"):
	if d:
		input.append(d)


inchars = ["ejp mysljylc kd kxveddknmc re jsicpdrysi",
	"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
	"de kr kd eoya kw aej tysr re ujdr lkgc jv"]

outchars = [ "our language is impossible to understand",
	"there are twenty six factorial possibilities",
	"so it is okay if you want to just give up"]


global anschar
anschar = {'z':'q','q':'z'}

for inchar,outchar in zip(inchars,outchars):
	if len(inchar) != len(outchar):
		print "Length unmathced!"
		sys.exit()
	for i in range(0,len(inchar)):
		if inchar[i] == " " and outchar[i] == " ": continue

		if inchar[i] not in anschar.keys():
			anschar[inchar[i]] = outchar[i]
		else:
			if anschar[inchar[i]] != outchar[i]:
				print "Different character!"
				print inchar
				print anschar
				sys.exit()
"""
print len(anschar)
for ans in sorted(anschar.keys()):
	print ans,":",anschar[ans],",",
"""

def problem(i):
	char = []
	for m in i:
		if m == " ":
			char.append(" ")
		else:
			char.append(anschar[m])

	return char


T = input[0]
#print T
global case_num
case_num = 1
for i in input[1:]:
	print "Case #%s: "%case_num,"".join(problem(i))
	case_num+=1
