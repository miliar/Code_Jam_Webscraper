import re


def main():
    filePrefix = 'A-large'
    fin = open(filePrefix + '.in', 'r')
    fout = open(filePrefix + '.out', 'w')
    L, D, N = [int(x) for x in (fin.readline().strip().split())]
    #print "L, D, N are %d, %d, %d" % (L, D, N)
    words = []
    for i in xrange(D):
        words.append(fin.readline().strip())
    #print "words are %s" % (words)
    for i in xrange(N):
        K = 0
        pat = re.compile(fin.readline().strip().replace('(', '[')
                         .replace(')', ']'))
        for j in xrange(D):
            if pat.match(words[j]):
                K += 1
        fout.write("Case #%d: %d\n" % ((i+1), K))
    fin.close()
    fout.close()


