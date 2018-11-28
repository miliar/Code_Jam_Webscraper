hits = 0

class SearchTreeNode:
    def __init__(self):
        self.children = {}
        self.letters = set()
        self.hits = 0

    def add_word(self, word):
        letter, tail = word[0], word[1:]
        if letter not in self.children:
            self.children[letter] = SearchTreeNode()
            self.letters.add(letter)
        if tail:
            self.children[letter].add_word(tail)

    def test_string(self, string):
        global hits
        if not string:
            assert not self.letters
            hits += 1
            return
        letters = set()
        if string[0] == '(':
            string = string[1:]
            while string[0] != ')':
                letters.add(string[0])
                string = string[1:]
            string = string[1:]
        else:
            letters.add(string[0])
            string = string[1:]
        for letter in letters.intersection(self.letters):
            self.children[letter].test_string(string)        

    def find_word(self, word):
        if not word:
            if not self.children:
                return True
            else:
                return False
        letter, tail = word[0], word[1:]
        if letter not in self.children:
            return False
        else:
            return self.children[letter].find_word(tail)
            

def process(filename):
    in_file = open(filename)
    L, D, N = map(int, in_file.readline().strip().split())

    dictionary = SearchTreeNode()
    for i in range(D):
        word = in_file.readline().strip()
        dictionary.add_word(word)

    global hits
    for i in range(N):
        hits = 0
        string = in_file.readline().strip()
        dictionary.test_string(string)
        print 'Case #%d: %d' % (i+1, hits)

if __name__ == '__main__':
    import sys
    process(sys.argv[1])
        

    
        
            
    
