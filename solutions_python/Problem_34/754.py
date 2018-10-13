import sys, string

class CompileError(Exception):
    pass

def compile(pattern):
    compiled = []
    inSet = False
    for c in pattern:
        if c == '(':
            inSet = True
            compiled.append([])
        elif c == ')':
            inSet = False
        else:
            if inSet:
                compiled[-1].append(c)
            else:
                compiled.append([c])
    return compiled

def check(pattern, word):
    if len(word) != len(pattern):
        return False
    for (w, p) in zip(word, pattern):
        if w not in p:
            return False
    return True

f = file(sys.argv[1])
numbers = f.readline()
numbers = string.split(numbers)
L = int(numbers[0])
D = int(numbers[1])
N = int(numbers[2])

words = []

for d in xrange(D):
    words.append(string.strip(f.readline()))

for n in xrange(N):
    pattern = compile(string.strip(f.readline()))
    count = 0
    for d in xrange(D):
        if check(pattern, words[d]):
            count += 1
    print 'Case #%d:'%(n+1), count

