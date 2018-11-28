class a_word(object):
    def __init__(self, length):
        self.length = length
        self.characters = [[] for x in range(self.length)]

    def could_be(self, str):
        for pos in range(self.length):
            if str[pos] in self.characters[pos]:
                pass
            else:
                return False
        return True



def make_word(str, length):
    n = 0
    in_paren = False
    wd = a_word(length)
    for char in str:
        if char == '(':
            in_paren = True
        elif char == ')':
            n += 1
            in_paren = False
        else:
            wd.characters[n].append(char)
            if not in_paren:
                n += 1
    return wd

print "File?"
file = open(raw_input())
word_len, dict_size, trials = [int(num) for num in file.readline().split()]

language = set()
for x in range(dict_size):
    language.add(file.readline().rstrip("\n"))

for y in range(trials):
    message = file.readline().rstrip("\n")
    wd = make_word(message, word_len)
    count = 0
    for poss in language:
        if wd.could_be(poss):
            count += 1
    print "Case #%s: %s" % (y+1, count)
