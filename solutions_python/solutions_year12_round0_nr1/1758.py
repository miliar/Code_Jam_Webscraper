f = open("A-small-attempt0.in", 'r')
g = open("output.out", 'w')
cases = int(f.readline())
i = 0
alfabet = {'a':'y','b':'h','c':'e','d':'s','e':'o','f':'c','g':'v','h':'x','i':'d','j':'u','k':'i','l':'g','m':'l','n':'b','o':'k','p':'r','q':'z','r':'t','s':'n','t':'w','u':'j','v':'p','w':'f','x':'m','y':'a','z':'q'}
 
while i<cases:
	out = ""
 	i = i+1
	for x in f.readline():
		if x == ' ':
			out = out + " "
		elif x != '\n':
			out = out + alfabet[x]
	print out
	g.write("Case #" + str(i) + ": " + out + "\n")
# 	array = []
# 	for x in f.readline().split():
# 		array.append(int(x))
# 	#print array
# 	googlers = array[0]
# 	surprises = array[1]
# 	limit = array[2]
# 	points = []
# 	n = 0
# 	while n<googlers:
# 		points.append(array[3 + n])
# 		n = n+1
# 	#print points
# 	answer = 0
# 	for uno in points:
# 		if (uno/3) >= limit: 
# 			answer = answer+1
# 		elif ((uno+2)/3) >= limit:
# 			answer = answer+1
# 		elif (surprises > 0) and (((uno+4)/3) >= limit) and (uno > 1) and (uno < 29) :
# 			answer = answer+1
# 			surprises = surprises -1
# 	print answer
# 	g.write("Case #" + str(i) + ": " + str(answer) + "\n")