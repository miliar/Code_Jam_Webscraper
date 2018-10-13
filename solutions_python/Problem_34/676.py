class Node():
    def __init__(self, letter='', children=[]):
        self.letter = letter
        self.children = []

infile = open("A-large.in", "r")
outfile = open("alien.out", "w")

line = infile.readline().split(" ")
wordlen, words, patterns = int(line[0]), int(line[1]), int(line[2])

wordlist = []
for i in xrange(words):
    wordlist.append(infile.readline())

root = Node()
for w in wordlist:
    pos = root
    for letter in w:
        match=False
        for c in pos.children:
            if c.letter == letter:
                match = True
                pos = c
        if match == False:
            child = Node(letter)
            pos.children.append(child)
            pos = child

def dfs_count(root, tokens):
    if len(tokens) == 0:
        return 1 # End of word
    elif len(root.children) == 0:
        return 0 # End of tree

    res = 0

    for t in tokens[0]:
        for c in root.children:
            if c.letter == t:
                res += dfs_count(c, tokens[1:])

    return res

for j in xrange(patterns):
    tokens = []
    i=0
    string = infile.readline()
    while i<len(string):
        token = ""
        if string[i] == "(":
            i+=1
            while string[i] != ")":
                token += string[i]
                i+=1
        else:
            token = string[i]

        tokens.append(token)
        i+=1

    outfile.write("Case #" + str(j+1) + ": " + str(dfs_count(root, tokens)) + "\n")
