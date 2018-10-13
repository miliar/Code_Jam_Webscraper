import sys, traceback

def maxVal(t, crit):
	if t < 2: return t
	if crit: return (t + 4) / 3
	else: return (t + 2) / 3

def evalEachCase (N, S, p, ti):
	ti.sort()
	ti.reverse()
	count = 0
	for t in ti:
		if maxVal(t, 0) >= p:
			count += 1
		elif S > 0 and maxVal(t, 1) >= p:
			count += 1
			S -= 1
	return str(count)

def main ():
	dir = "C:/Users/Firman/Documents/Programming/Python/GoogleCodeJam/2012/Qualification/"
	fin = open (dir+"B-large-practice.in", "r") # nama file input
	fout = open (dir+"B-large-practice.out", "w") # nama file output
	
	content = fin.read()
	lines = content.split('\n')
	
	n = eval(lines.pop(0))
	
	linesOut = []
	for i in range (n):
		line = lines.pop(0)
		args = line.split()
		N = eval(args.pop(0))
		S = eval(args.pop(0))
		p = eval(args.pop(0))
		ti = []
		for j in range(N):
			ti.append(eval(args.pop(0)))
		linesOut.append ("Case #" + str(i+1) + ": " + evalEachCase (N, S, p, ti) )
	
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
