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
    lines = (input.readline().rstrip('\n') for i in range(numLines))
    for (i,line) in enumerate(lines):
        print 'Case #%d: %s'%(i+1, str(evaluate(line)))

def csplit(line, separator):
    for part in line.split(separator):
        try:
            yield int(part)
        except:
            yield str(part)

def evaluate(line):
    (numStalls, numPeople) = csplit(line, ' ')
    spaces_map = {numStalls:1}
    val1 = 0
    val2 = 0
    for i in range(numPeople):
        max_spaces = max(spaces_map.keys())
        max_count = spaces_map[max_spaces]
        if max_count > 1:
            spaces_map[max_spaces] -= 1
        else:
            del spaces_map[max_spaces]

        val1 = (max_spaces-1)/2
        val2 = val1 + (1 if (max_spaces-1)%2==1 else 0)
        for val in (val1, val2):
            if (val > 0):
                count = spaces_map[val] if spaces_map.has_key(val) else 0
                spaces_map[val] = count+1
    return str(val2) + ' ' + str(val1)
main()

