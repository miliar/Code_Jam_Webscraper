

sentence = "zqejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv".replace(" ","")

l_sen = len(sentence)

trans = "qzour language is impossible to understand there are twenty six factorial possibilitiesso it is okay if you want to just give up".replace(" ","")


def t(char):
	for x in xrange(l_sen):
		if char == sentence[x]:
			return trans[x]		
	return " "

total = raw_input()

for counter in xrange(int(total)):
	line = raw_input()
	output = ""
	for c in xrange(len(line)):	
		output = output + t(line[c])
	#print(output)
 	print("Case #" + str(counter+1) + ": " + output)



