import sys, traceback

def evalEachCase (line0):
	# from googlerese to english
	maps = {' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q'}
	strOut = ""
	for c in line0: strOut += maps[c]
	return strOut

def main ():
	dir = "C:/Users/Firman/Documents/Programming/Python/GoogleCodeJam/2012/Qualification/"
	fin = open (dir+"A-small-practice.in", "r") # nama file input
	fout = open (dir+"A-small-practice.out", "w") # nama file output
	
	content = fin.read()
	lines = content.split('\n')
	
	n = eval(lines.pop(0))
	
	linesOut = []
	for i in range (n):
		linesOut.append ("Case #" + str(i+1) + ": " + evalEachCase (lines[i]) )
	
	contentOut = "\n".join(linesOut)
	fout.write(contentOut)
	
	fin.close()
	fout.close()

try:
	main()
except:
	exc_type, exc_value, exc_traceback = sys.exc_info()
	print traceback.print_tb(exc_traceback)
	print traceback.print_exception(exc_type, exc_value, exc_traceback)
	raw_input()
