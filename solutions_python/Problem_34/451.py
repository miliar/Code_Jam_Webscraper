import sys

f = file(sys.argv[1], "r")
out = file(sys.argv[1][:-2] + "out","w")

def read_int_line():
    return int(f.readline().strip())

def read_int_list_line(sep = " "):
    return [int(i) for i in f.readline().strip().split(sep)]

def read_word():
    return f.readline().strip()        

def parse_pattern(pattern):
    word = []
    for i in xrange(L):
        word.append(set())

#    print word
    pos = 0
    state = "s"
    while len(pattern):
        #print pos, pattern, word
        if pattern[0] == "(":
            state = "m"
        elif pattern[0] == ")":
            state = "s"
            pos = pos + 1
        else:
            c = pattern[0]
            word[pos].add(c)            
            if state == "s":
                pos = pos + 1
        pattern = pattern[1:]
    return word

(L,D,N) = read_int_list_line()
dict = set()
for i in xrange(D):
    w = read_word()
    #print "Word", w
    dict.add(w)

def check_word(word):
    for i in xrange(len(word)):
        c = word[i]
        if not c in word_pattern[i]:
            #print "Word %s is invalid" % word
            return False
    return True

for test_case in xrange(1,N+1):
   # print "Test case", test_case
    pattern = read_word()
    word_pattern = parse_pattern(pattern)
    #print word_pattern
    valid = 0
    for word in dict:
       # print word
        if check_word(word):
            valid = valid + 1
    r = "Case #%s: %s" % (test_case, valid)
    print r
    out.write(r + "\n")