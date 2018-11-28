import sys
import re

class AlienCounter(object):
    def __init__(self, known_words):
        self.known_words = known_words
    def word_count(self, r):
        r = r.replace('(', '[')
        r = r.replace(')', ']')
	r = re.compile(r)
        #sys.stderr.write('known_words: %s\n' % str(self.known_words))
        return sum(bool(r.match(s)) for s in self.known_words)
    def do_one_test_case(self, file):
        s = file.readline().strip()
        return self.word_count(s)

def main(argv):
    f = open(argv[1], 'r')
    L, D, cases = (int(n) for n in f.readline().split())
    #sys.stderr.write('L: %d\n' % L)
    #sys.stderr.write('D: %d\n' % D)
    sys.stderr.write('Cases: %d\n' % cases)
    valid_words = []
    for i in xrange(D):
        valid_words.append(f.readline().strip())
    alien_counter = AlienCounter(valid_words)
    do_one_test_case = alien_counter.do_one_test_case
    output_list = []
    for i in xrange(cases):
        output_list.append('Case #%d: %s\n' % (i+1, do_one_test_case(f)))
        sys.stderr.write('%d of %d done\n' % (i+1, cases))
    f.close()
    if len(argv) > 2:
        expected_f = open(argv[2], 'r')
        expected_list = expected_f.readlines()
        expected_list = [line.strip()+'\n' for line in expected_list[0:-1]]
        if (output_list == expected_list):
            print 'Everything matched!'
        else:
            print 'Actual: %s' % output_list
            print 'Expected: %s' % expected_list
    else:
        print ''.join(output_list)

def test():
    print 'Usage: scriptname.py infile [outfile]'
    print 'I\'ll run the doctests instead!'
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        test()
    else:
        main(sys.argv)
