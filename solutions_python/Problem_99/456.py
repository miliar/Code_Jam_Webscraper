import operator
import string
import sys

def abortTrying(chars):
	return 1 + chars + 1


def keepTrying(probs, charsRemaining, charsTyped):
	failCase = charsRemaining+1+charsTyped+charsRemaining+1
	winCase = charsRemaining+1

	p = reduce(operator.mul, probs)

	return (p*winCase+(1-p)*failCase)

def backspaces(probs, charsRemaining, charsTyped):
	curBest = sys.maxint

	for i in xrange(1,charsTyped):
		fail = 2*i+charsRemaining+1+charsTyped+charsRemaining+1
		win = 2*i + charsRemaining + 1

		p = reduce(operator.mul, probs[0:-i])
		expected = p*win + (1-p)*fail

		curBest = min(curBest, expected)
	
	return curBest


def solveCase(probs, remaining, typed):
	carryon = keepTrying(probs, remaining, typed)
	abort = abortTrying(remaining+typed)
	backspace = backspaces(probs, remaining, typed)

	return min(carryon, abort, backspace)


#Standard CodeJam input munching
def codejam():
	lines = sys.stdin.readlines()
	numcases = int(lines[0])

	for c in xrange(1,numcases+1):
		line = lines[(2*c)-1].split(" ")
		typed = int(line[0])
		remaining = int(line[1]) - typed
		probs = map(float, lines[2*c].split(" "))
		val = solveCase(probs, remaining, typed)
		ans = string.join(["Case #",str(c),": %0.6f" % val,"\n"], '')
		sys.stdout.write(ans)

codejam() 
