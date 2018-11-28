fi = open("jamtest.txt","r")
fo = open("jamout.txt","w")

d = {'a':'y','b':'h','c':'e','d':'s','e':'o','f':'c','g':'v','h':'x','i':'d','j':'u','k':'i','l':'g','m':'l','n':'b','o':'k','p':'r','q':'z','r':'t','s':'n','t':'w','u':'j','v':'p','w':'f','x':'m','y':'a','z':'q'}

lines = fi.readlines()
lines = lines[1:len(lines)]
case = 1

for line in lines : 
	new = ""
	for c in line.strip():
		if c == ' ':
			new = new + ' '
		else:
			new = new + d[c]
	fo.write("Case #" + str(case) + ": " + new + "\n")
	case = case + 1

fo.close()