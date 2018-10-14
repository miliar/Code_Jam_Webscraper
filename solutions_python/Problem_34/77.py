import sys

def filter_letters(word_set, words, n, test):
    f = lambda x: words[x][n] in test
    return filter(f, word_set)

f = open(sys.argv[1], "r")
line = f.readline()
L, D, N = map(lambda x: int(x), line.split())
words = []
for d in xrange(D):
    words.append( f.readline().strip() )    

for n in xrange(N):
    test =  f.readline().strip()
    valid = []
    #parse the test
    x = 0
    while  x < len(test):
        if test[x] == '(':
            x += 1
            letter_test = []
            while test[x] != ')':
                letter_test.append(test[x])
                x += 1
            valid.append(letter_test)
        else:
            valid.append([test[x]])
        x += 1
    word_set = xrange(len(words))
    lettern = 0
    for vletters in valid:
        word_set = filter_letters(word_set, words, lettern, vletters)
        lettern += 1
    cases = len(word_set)
    print "Case #%d: %d" % (n+1, cases)
