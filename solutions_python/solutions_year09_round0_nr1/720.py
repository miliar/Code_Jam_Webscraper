
class Lang(object):
    def __init__(self, num_letters, words):
        self.num_letters = num_letters
        self.words = words


    def count(self, word_input):
        word = self._parse_word(word_input)
        #print "parsed", word
        vocab = self.words[:]
        count = 0

        for pos, letter in enumerate(word):
            vocab = [w for w in vocab if w[pos] in letter]
        return len(vocab)


    def _parse_word(self, word_input):
        word = []
        in_group = False

        for letter in word_input:
            if letter == '(':
                word.append([])
                in_group = True
            elif letter == ')':
                in_group = False
            elif in_group:
                word[-1].append(letter)
            else:
                word.append([letter])
        return word



def test_sample(data):
    n_letters, n_words, n_tests = data[0].split()
    words = [w.strip() for w in data[1:(int(n_words)+1)]]
    lang = Lang(n_letters, words)

    result = []
    for case in data[-int(n_tests):]:
        result.append(lang.count(case.strip()))
    return result


if __name__ == "__main__":
    import sys
    FILE_IN = sys.argv[1]

    inp = open(FILE_IN, 'r')
    lines = inp.readlines()
    inp.close()

    result = test_sample(lines)

    outp = open(FILE_IN[:-2]+'out', 'w')
    count = 1
    for res in result:
        outp.write("Case #%d: %s\n" % (count,res))
        count += 1
    outp.close()



