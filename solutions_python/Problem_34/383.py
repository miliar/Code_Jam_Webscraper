def recursiveGenerator(dict, word, wordGen, index, wordCount):
    for c in wordGen[index]:
        newword = word + c
        if index == len(wordGen) - 1:
            if newword in dict:
                wordCount += 1
        else:
            foundCompatible = False
            for w in dict:
                if w.startswith(newword):
                    foundCompatible = True
                    break
            if foundCompatible:
                wordCount = recursiveGenerator(dict, newword, wordGen, index + 1, wordCount)
    return wordCount
            

infile = open("../A-small-attempt1.in", "r")
outfile = open("../A-small-attempt1.out", "w")
(L, D, N) = [int(n) for n in infile.readline().split()]
dict = []
for i in range(D):
    dict.append(infile.readline().strip())
outputLines = []
for i in range(N):
    wordGen = []
    text = infile.readline().strip()
    multiple = False
    for c in text:
        if c == '(':
            multiple = True
            wordGen.append([])
        elif c == ')':
            multiple = False
        else:
            if not multiple:
                wordGen.append([])
            wordGen[-1].append(c)
    outputLines.append("Case #" + str(i + 1) + ": " + str(recursiveGenerator(dict, "", wordGen, 0, 0)))
outfile.write("\n".join(outputLines))
