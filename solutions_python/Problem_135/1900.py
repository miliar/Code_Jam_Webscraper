
import sys
def read():  sys.stdout.flush(); return sys.stdin.readline().strip()

tests = int(read())
for test in xrange(tests):
	choice1 = int(read())
	rows1 = [read().split(" "), read().split(" "),
			 read().split(" "), read().split(" ")]
	choice2 = int(read())
	rows2 = [read().split(" "), read().split(" "),
			 read().split(" "), read().split(" ")]
	
	possibles = set(rows1[choice1-1]) & set(rows2[choice2-1])
	if len(possibles) == 1:
		result = str(list(possibles)[0])
	elif possibles:
		result = "Bad magician!"
	else:
		result = "Volunteer cheated!"
	print "Case #%d: %s" % (test+1, result)

