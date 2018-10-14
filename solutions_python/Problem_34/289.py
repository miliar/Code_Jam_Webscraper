import re

INPUT = 'A-large.in'
OUTPUT = 'A-large.out'

def countWords(token, words):

    token = token.replace('(', '[')
    token = token.replace(')', ']')
    m = 0
    token = re.compile(token)
    for word in words:
        if token.match(word):
            m += 1
    return m

def readWords(D, fobj):

    words = []
    for i in range(D):
        words.append(fobj.readline().strip())
    return words


if __name__  == '__main__':

    fobj = open(INPUT)
    L,D,N = [int(i) for i in fobj.readline().strip().split()]
    words = readWords(D, fobj)
    tokens = readWords(N, fobj)
    output = open(OUTPUT, 'w')
    for i in xrange(len(tokens)):
        m = countWords(tokens[i], words)
        output.write('Case #%d: %d\n' % (i+1, m))
    output.close()
    fobj.close()
        
    
