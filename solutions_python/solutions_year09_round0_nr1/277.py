import sys


def set_gen (s):
    curs = None
    for c in s:
        if c == '(':
            assert curs == None
            curs = set()
        elif c == ')':
            assert curs != None
            assert len(curs) > 0
            yield curs
            curs = None
        else:
            if curs != None:
                curs.add(c)
            else:
                yield set(c)


def test_word(word, processed_exp):
    for c,s in map(None, word, processed_exp):
        #print c,s
        if not c in s:
            return False
    return True
        
            
def test_words (words, processed_exp):
    count = 0
    for word in words:
        if test_word(word, processed_exp):
            count += 1
    return count
    

def read_file(filename):
    with open(filename) as f:
        (L,D,N) = [int(x) for x in f.readline().strip().split(' ')]
        words = []
        for i in range(D):
            words.append(f.readline().strip())
            assert len(words[i]) == L, len(words[i])
        assert len(words) == D
        for test_case in range(N):
            l = [ss for ss in set_gen(f.readline().strip())]
            #print l
            assert len(l) == L,  l
            print "Case #%d: %d" % (test_case+1, test_words(words, l))

if __name__ == "__main__":
    read_file(sys.argv[1])      
        
        

            
            
                
        