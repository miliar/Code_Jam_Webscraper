



class Translator:
    mappingOriginal = {
        'a' : 'y',
        'o' : 'e',
        'z' : 'q',
        's' : 'd',
        'u' : 'j',
        }

    mapping = {'a': 'y', 'c': 'f', 'b': 'n', 'e': 'c', 'd': 's', 'g': 'v',
               'f': 'w', 'i': 'k', 'h': 'b', 'k': 'i', 'j': 'u',
               'm': 'x', 'l': 'm', 'o': 'e', 'n': 's', 'q': 'z', 'p': 'v',
               's': 'd', 'r': 'p', 'u': 'j', 't': 'r', 'w': 't', 'v': 'p',
               'y': 'a', 'x': 'h', 'z': 'q', ' ' : ' '}

    reverseMapping = {' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o',
                      'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x',
                      'k': 'i', 'j': 'u',
                      'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p':
                      'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 
                      'v': 'p', 'y': 'a', 'x': 'm', 'z' : 'q'}
    def __init__(self):
        #self.reverseMapping = dict((v,k) for k,v in self.mapping.iteritems())
        pass

    def buildMapping(self):
        examples = {
            'a zoo' : 'y qee',
            'our language is impossible to understand' :
                'ejp mysljylc kd kxveddknmc re jsicpdrysi',
            'there are twenty six factorial possibilities' :
                'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd',
            'de kr kd eoya kw aej tysr re ujdr lkgc jv' :
            'so it is okay if you want to just give up',
            }

        self.mapping = {}
        for english, googlerese in examples.iteritems():
            for i in xrange(0, len(english)):
                self.mapping[ english[i] ] = googlerese[i]
                self.reverseMapping[ googlerese[i] ] = english[i]


        print self.reverseMapping

        for x in xrange(0, 26):
            letter = chr(ord('a') + x)

            if letter not in self.mapping:
                self.mapping[letter] = self.reverseMapping[letter]

        for x in xrange(0, 26):
            letter = chr(ord('a') + x)
            assert letter in self.mapping, letter

    def toEnglish(self, googlereseString):
        """Translates from Googlerese to English"""

        def _mapping(c):
            return c if c not in self.reverseMapping else self.reverseMapping[c]

        return ''.join( map( _mapping, googlereseString ) )

    def toGooglerese(self, englishString):
        """Translates from English to Googlerese"""
       pass

def main():
    t = Translator()

    # Check to ensure we can translate all letters.
    for x in xrange(0, 26):
        letter = chr(ord('a') + x)
        assert letter in t.reverseMapping, letter

    with open('input.txt') as fs:
        testCases = int(fs.readline())

        for testCase in xrange(0, testCases):
            line = fs.readline()
            print "Case #%d: %s" % (testCase+1, t.toEnglish(line.strip()))

if __name__ == "__main__":
    main()
