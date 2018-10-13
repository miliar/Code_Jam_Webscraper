import re, string

par2bracket = string.maketrans('()', '[]')

def readInput(f):
    allLines = open(f, 'r').readlines()
    L, D, N = map(int, allLines[0].split())
    allWords = "".join(allLines[1:1+D])
    patterns = allLines[1+D:]
#    print "allWords: \n", allWords
#    print "patterns: \n", patterns
    return L, D, N, allWords, patterns

def countMatch(words, pattern):
    p = pattern.strip().translate(par2bracket)
    return len(re.findall(p, words))

def main(f):
    L, D, N, allWords, patterns = readInput(f)
    count = 1
    for x in patterns:
        print "Case #%d: %d" % (count, countMatch(allWords, x))
        count += 1

if __name__=='__main__':
    import sys
    main(sys.argv[1])
    
    
