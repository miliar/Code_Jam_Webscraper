import sys

def study():
	mapper= {}
	first = "ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jvy qee"
	second = "our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give upa zoo"

	for i in range(0,len(first)):
		mapper[first[i]] = second[i]
	
	# gotta get a value for mapping z
	values = mapper.values()
	check = [chr(i+97) for i in range(0,26)]
	check = filter(lambda a: a not in values, check)
	mapper['z'] = check[0]

	return mapper

infile = open(sys.argv[1]).read().splitlines()[1:]

mapper = study()

for i in range(0,len(infile)):
	new_str = ""
	for j in infile[i]:
		new_str += mapper[j]
	print "Case #" + str(i+1) + ": " + new_str
