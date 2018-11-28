infile = open("A-large.in","r")
outfile = open("A-large.out","w")
LDN = infile.readline().strip().split(" ")
L = int(LDN[0])
D = int(LDN[1])
N = int(LDN[2])

def addtodict(subword, subdict):
    if subword == "":
        return
    if subword[0] not in subdict:
        subdict[subword[0]] = {}
    addtodict(subword[1:],subdict[subword[0]])

def checkdict(subwordposs, subdict):
    if subwordposs == []:
        return 1
    entries = 0
    for letter in subwordposs[0]:
        if letter in subdict:
            entries += checkdict(subwordposs[1:],subdict[letter])
    return entries

words = {}
for i in range(D):
    word = infile.readline().strip()
    addtodict(word, words)

for i in range(N):
    pattern = infile.readline().strip()
    wordposs = []
    while pattern != "":
        if pattern[0] == "(":
            token,dummy,pattern = pattern.partition(")")
            wordposs.append(token)
        else:
            wordposs.append(pattern[0])
            pattern = pattern[1:]
    matches = checkdict(wordposs,words)
    out = "Case #" + str(i+1) +": " + str(matches) + "\n"
    print out
    outfile.write(out)    

infile.close()
outfile.close()
