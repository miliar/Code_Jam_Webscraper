#3
#elcomew elcome to code jam
#wweellccoommee to code qps jam
#welcome to codejam


def count(line, text):
	#print "Got line:",line
	#print "Got text:",text
	if line and text:
		if len(line) < len(text):
			return 0
		if len(text) == 1 and line[0] == text:
			return 1# + count(line[1:], text)
		
		total = 0
		letter = text[0]
		#print "Letter:",letter
		for i in range(len(line)):
			if line[i] == letter:
				#print "line[%d]=letter=%s" % (i, letter)
				line_to_send = line[i:]
				if len(text) > 1:
					text_to_send = text[1:]
				else:
					text_to_send = text
				#print
				#print "Calling with:"
				#print "Line:", line_to_send, "Text:", text_to_send
				a = count(line_to_send,text_to_send)
				
				#print a
				#print
				total += a
				
		return total

	return 0

f = open("C-small-attempt3.in")
g = open("CSMALL-3.out", "w")

lines = []

#print count("wwwelcommmeee to cccode jamymm","welcome to code jam")

N = int(f.readline().strip("\n"))
for i in range(N):
	line = f.readline().strip("\n")
	#print "Case #%d: %04d" % (i+1, count(line, "welcome to code jam")%10000)
	g.write("Case #%d: %04d\n" % (i+1, count(line, "welcome to code jam") % 10000))
	
	
	
g.close()
