def read(filename):
    input = open(filename, 'r')
    
    text_num = int(input.readline())
    texts = []
    
    for i in xrange(text_num):
        texts.append(input.readline().strip())
        
    return texts

def count(text, sub, i):
    if len(sub) == 0:
        return 1
    index = text.find(sub[0])
    occurences = 0
    while index >= 0: 
        text = text[index + 1:]
        occurences += count(text, sub[1:], i + 1)
        index = text.find(sub[0])
    return occurences

def last_digits(number):
    return int(str(number)[-4:])

if __name__ == "__main__":
    texts = read('C-small-attempt0.in')
    for index, text in enumerate(texts):
        print "Case #%d: %04d" % ((index + 1), last_digits(count(text, "welcome to code jam", 0)))