#Mapping########
input1 = """ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv"""
output1="""our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up"""
newline = input1[40]
space = input1[3]
len1 = len(input1)
code_in = []
code_out = []
import string
for stuff in string.ascii_lowercase:
	for item in range(len1):
		if output1[item] == stuff:
			code_in.append(stuff)
			code_out.append(input1[item])
			break
code_in.append("z")
code_out.append("q")
code_in.append("q")
code_out.append("z")
#code_in.append(space)
#code_out.append(space)
#Mapping end####

f_in = open('/home/anirudh/codejam/q1', 'r')
f_out = open('/home/anirudh/codejam/q1_output', 'w')

num = int(f_in.readline())

for x in range(num):
	f_out.write("Case #"+str(x+1)+": ")
	line = f_in.readline()
	len2 = len(line)
	for item in range(len2):
		for stuff in range(26):
			if line[item] == code_out[stuff]:
				f_out.write(code_in[stuff])
			if line[item] == space:
				f_out.write(" ")
				break
	f_out.write(newline)
