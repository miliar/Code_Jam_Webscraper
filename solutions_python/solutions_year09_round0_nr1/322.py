import re

def read_file(filename):
    dictionary = []
    
    input = open(filename, 'r')
    
    l, d, n = map(int, input.readline().split(" "))

    for i in xrange(d):
        entry = input.readline().strip()
        if len(entry) == l:
            dictionary.append(entry)
        
    words = []
    for i in xrange(n):
        words.append(input.readline().strip())
    
    input.close()
    
    return l, dictionary, words

def check_word(message, length, dictionary):
    regex = ""
    open_par = False
    for index, letter in enumerate(message):
        if open_par and letter != ")" and message[index - 1] != "(":
            regex += "|"
        if letter == "(":
            open_par = True
        if letter == ")":
            open_par = False
        regex += letter
        
    total = 0
    for word in dictionary:
        if re.match(regex, word):
            total = total + 1
    return total

     
if __name__ == "__main__":
    length, dictionary, words = read_file('A-small-attempt1.in')
    for index, word in enumerate(words):
        total = check_word(word, length, dictionary)
        print "Case #%d: %d" % (index + 1, total)
