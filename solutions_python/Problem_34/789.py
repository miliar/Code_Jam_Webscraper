
def parse_line(line, dic, index):
	if len(dic) == 0:
		return 0
	if len(line) == 0:
		return len(dic)
	place = line.find('(')
	dicT = []
	if place == -1:
		for word in dic:
			if word[index:] == line:
				dicT += [word]
		return len(dicT)
	before = ""
	if place != 0:
		before = line[0:place]
		for word in dic:
			if word[index:index+place] == before:
				dicT += [word]
	else:
		dicT = dic
	dicTemp = []
	placeEnd = line.find(')')
	for i in range(place+1,placeEnd):
		for word in dicT:
			if word[index+len(before)] == line[i]:
				dicTemp += [word]
	return parse_line(line[placeEnd+1:], dicTemp, index + place+1)


	
file = open("c:\input.txt")
dic = []
params = file.readline().split(' ')
for i in range(0, int(params[1])):
	dic += [file.readline().strip()]

for j in range(1, int(params[2])+1):
	words = parse_line(file.readline().strip(), dic,0)
	print "Case #%s: %s" %(j,words)
#print parse_line("a(jmu)(knce)a(koqt)eru(twhp)f",dic,0)


	
