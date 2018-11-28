import sys
import os, stat

def main():
    mode = os.fstat(0).st_mode
    input = None
    if stat.S_ISFIFO(mode):
        #print "stdin is piped"
        input = open("input.txt")
    elif stat.S_ISREG(mode):
        #print "stdin is redirected"
        input = sys.stdin
    else:
        #print "stdin is terminal"
        input = open("input.txt")

    numLines = int(input.readline())
    lines = (input.readline() for i in range(numLines))
    i = 0
    for line in lines:
        i+=1
        print 'Case #%d: %s'%(i, str(evaluate(line)))


def evaluate(line):
    def flip(pancakes, i, width):
        return pancakes[:i] + ''.join(('-'  if pancake == '+' else '+') for pancake in pancakes[i:i+flipperWidth]) + pancakes[i+flipperWidth:]

    parts = line.split(' ')
    pancakes = parts[0]
    flipperWidth = int(parts[1])
    flipCount = 0
    for i in range(len(pancakes) - flipperWidth + 1):
        if pancakes[i] == '-':
            pancakes = flip(pancakes, i, flipperWidth)
            flipCount += 1
    if '-' in pancakes:
        return 'IMPOSSIBLE'
    return flipCount

main()

