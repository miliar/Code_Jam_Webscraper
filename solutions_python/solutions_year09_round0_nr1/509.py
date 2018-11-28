def tokenize(line):
    tokens = []
    while len(line) > 0:
        if line[0] == '(':
            end = line.find(')')
            tokens.append(line[1:end])
            line = line[end + 1:]
        else:
            tokens.append(line[0])
            line = line[1:]

    return tokens

INPUT = open('A-large.in')
OUTPUT = open('A-large.out', 'w')

L, D, N = INPUT.readline().split()
L, D, N = int(L), int(D), int(N)

words = []
for i in range(D):
    line = INPUT.readline().strip()
    words.append(line)

for i in range(N):
    print(i)
    line = INPUT.readline().strip()
    tokens = tokenize(line)

    words_copy = words[:]
    for j in range(len(tokens)):
        token = tokens[j]
        for word in words_copy[:]:
            if word[j] not in token:
                words_copy.remove(word)


    print >> OUTPUT, "Case #" + str(i + 1) + ": " + str(len(words_copy))

INPUT.close()
OUTPUT.close()
