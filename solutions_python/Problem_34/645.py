import sys
import re
test_splitter = re.compile(r"[a-z]|\([a-z]+\)")

class Trie(object):
    def __init__(self, letter = ""):
        self.letter = letter
        self.next   = {}
        self.word   = False
        
    def add_word(self, word):
        if len(word) == 0:
            self.word = True
            return
            
        letter = word[0]
        if not letter in self.next.keys():
            self.next[letter] = Trie(letter)
        self.next[letter].add_word(word[1:])
    
    def count_matches(self, parts_list):
        """[[letter]] -> Integer"""
        if len(parts_list) == 0:
            return self.word
            
        sum = 0
        for letter in parts_list[0]:
            if letter in self.next.keys():
                sum += self.next[letter].count_matches(parts_list[1:])
        
        return sum 

    def debug(self, indent = 0):
        """Print out the trie for debugging."""
        print "|-"*indent + self.letter
        for next in self.next.values():
            next.debug(indent + 1)
            
def parse(input):
    """[lines of input] -> ([word list], [test cases])"""
    letters, wordcount, testcount = map(int, input[0].split())
    words     = map(lambda w: w.strip("\n"), input[1:wordcount+1])
    raw_tests = map(lambda w: w.strip("\n"), input[wordcount+1:])
    
    #parse the tests for trie matching
    tests = []
    for raw_test in raw_tests:
        test = test_splitter.findall(raw_test)
        test = map(lambda s: s.strip("()"), test)
        
        if test != []:
            tests.append(test)
    
    return (words, tests)
    
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print >>sys.stderr, "Usage:\n\tpython AlienLanguage.py input_file.txt"
        exit(-1)
        
    input_filename = sys.argv[1]
    file  = open(input_filename, "r")
    lines = file.readlines()
    file.close()
    
    words, tests = parse(lines)
    
    #print >>sys.stderr, "WORDS:", words
    #print >>sys.stderr, "TESTS:", tests
    
    t = Trie()
    for word in words:
        t.add_word(word)
        
    for i, test in enumerate(tests):
        print "Case #%d:" % (i+1), t.count_matches(test)
        


