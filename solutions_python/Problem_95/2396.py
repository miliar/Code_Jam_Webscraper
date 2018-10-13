gmap = {}

input_G = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jvqz "
input_E = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give upzq "

for i in xrange(0, len(input_G)): #assumed to be the same length as input_E
	gmap[input_G[i]] = input_E[i]

gmap["0"] = ""
print gmap

f = open("A-small-attempt1.in")
input = f.readlines()

output = ""

for i in xrange(1,int( input[0])+1):
	output += "Case #" + str(i) + ": "
	for l in input[i][:len(input[i])-1]:
		output += gmap[l]	
	output += "\n"

f = open("problema.out", "w")
f.write(output)
f.close()
