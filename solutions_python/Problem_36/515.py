import string

def recur( line, expr):
        c = expr[0]
	match = 0
	index = 0
#	print "c = ",c
#	print "line = ",line
#	print "expr = ",expr
        if len(expr) == 1:
#                print "REACHED BASE CASE"
#               print "returning ",string.count(line, c)
		return string.count(line, c)
        index = string.find(line, c)
        if index == -1:
#               	print "Line: "+line+" doesnt contain ",c
                return 0;
        while index != -1:
#		print "MATCH before recur: ",match
		match = recur(line[index+1:], expr[1:]) + match
#		print "MATCH after recur: ",match
		line = line[index+1:]
		index = string.find(line, c)
        return match


filename = "C-small-attempt2.in"
input = open(filename, "r")
cases = int(input.readline())
for i in range(cases):
	line = string.strip(input.readline(),"\n")
	ans = recur(line, "welcome to code jam")
	if ans > 10000:
                        sm = str(ans)
                        sm = sm[-4:-1]
                        ans = int(sm)
	print "Case #"+str(i+1)+": "+string.zfill(str(ans),4)

