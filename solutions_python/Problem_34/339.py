def solve(sentence, words, L):
    #print "solve(" + sentence + ", " + str(words) + ", " + str(L) + ")"
    tokens = parse(sentence)
    out = 0

    for word in words:
        for x in range(L):
            works = True
            if word[x] not in tokens[x]:
                works = False
                break
        if works:
            out += 1

    return out

def parse(sentence):
    #print "parse(" + sentence + ")"
    tokens = []
    sentence = list(sentence)
    while len(sentence) > 0:
        token = sentence.pop(0)
        if token == "(":
            token = ""
            while True:
                char = sentence.pop(0)
                if char == ")":
                    break
                token += char
        tokens.append(token)
    return tokens

f = open("A-large.in.txt", "r")
header = f.readline().split()

L = int(header[0].strip())
D = int(header[1].strip())
N = int(header[2].strip())

words = []
for x in range(D):
    words.append(f.readline().strip())

for x in range(N):
    print "Case #" + str(x+1) + ": " + str(solve(f.readline().strip(), words, L))
