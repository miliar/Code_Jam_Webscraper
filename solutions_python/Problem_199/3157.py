import sys

def flip(c):
    return '+' if c == '-' else '-'

def min_flips(stack, k):
    if len(stack) == k:
        if all(c == '-' for c in stack):
            return 1
        elif all(c == '+' for c in stack):
            return 0
        raise Exception()
    
    if stack[0] == '+':
        return min_flips(stack[1:], k)
        
    else:
       stack = ''.join(([flip(c) for c in stack[1:k]])) + stack[k:]
       return 1 + min_flips(stack, k)

with open(sys.argv[1]) as infile:
    infile.readline()
    for index, line in enumerate(infile, 1):
        stack = line.split()[0]
        k = int(line.split()[1])
        try:
            print 'Case #%d: %d' % (index, min_flips(stack, k))
        except Exception as error:
            print 'Case #%d: IMPOSSIBLE' % index
