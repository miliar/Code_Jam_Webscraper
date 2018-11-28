import fileinput

def replace_all(text, dic):
    for i, j in dic.iteritems():
        print i+" to "+j
        text = text.replace(i, j)
    return text

reps = {'a':'y', 'o':'k', 'z':'q', 'd':'s', 'k':'i', 'v':'p', 'j':'u', 's':'n', 'l':'g', 'g':'v', 'r':'t', 'x':'m', 'y':'a', 'b':'h', 'p':'r', 'e':'o', 'c':'e', 'f':'c', 'm':'l', 'n':'b', 'i':'d', 't':'w', 'h':'x', 'w':'f', 'u':'j', 'q':'z'}

counter = 1
aux = ""
for line in fileinput.input():
	for l in line.rstrip():
		if l != " ":
			aux = aux+reps[l]
		else:
			aux = aux+" "
	print "Case #"+str(counter)+":"+" "+aux
	aux = ""
	counter = counter+1
