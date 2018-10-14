import sys

sys.setrecursionlimit(15000)

infile = open('input.txt', 'r')
outfile = open('out.txt', 'w')

first_line = infile.readline()
first_line = first_line.split(' ')

tokens = int(first_line[0])
words_in_dictionary = int(first_line[1])
test_cases = int(first_line[2])

print tokens
print words_in_dictionary
print test_cases

dictionary=[]
for word in range(words_in_dictionary):
    w = infile.readline()
    if(w[len(w)-1]=='\n'):
        w=w[:-1]
    dictionary.append(w)


word = []
result = []
matches = 0

def find(curr_token, w=''):
    global match
    if curr_token == tokens:
        if dictionary.__contains__(w):
            if not result.__contains__(w):
                print w
                match += 1
                result.append(w)
        return
    for t in word[curr_token]:
        new_w = w + t
        len_new_w = len(new_w)
        for d in dictionary:
            if new_w==d[:len_new_w]:
                find(curr_token + 1, new_w)


for case in range(test_cases):
    word = []
    result = []
    match = 0

    for t in range(tokens):
        word.append([])

    pattern = infile.readline()
    if(pattern[len(pattern)-1]=='\n'):
        pattern=pattern[:-1]

    token_position = 0
    i = 0
    while True:
        if(pattern[i] == '('):
            end = pattern.find(')',i)
            sub = pattern[i+1:end]
            for s in sub:
                word[token_position].append(s)
            i = end + 1
        else:
            word[token_position].append(pattern[i])
            i += 1
        token_position += 1
        if i == len(pattern):
            break

    find(0)

    outfile.write("Case #%d: %d\n" % (case+1, match))


    print "done"

infile.close()
outfile.close()
