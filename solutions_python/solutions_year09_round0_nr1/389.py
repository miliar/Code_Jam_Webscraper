import sys

filename = sys.argv[1]
#print "Using file", filename
input = open(filename, 'r')
outputname = filename[:-2] + "out"
output = open(outputname, 'w')

length, numwords, cases = [int(x) for x in input.readline().split()]
#print "length:", length, "numwords:", numwords, "cases:", cases

words = []
for i in range(numwords):
    words.append(input.readline()[:-1])
#print words
    
for case in range(1, cases + 1):
    output.write("Case #" + str(case) + ": ")

    currline = input.readline()[:-1]
    #print "Case", case, "line:", currline
    tokens = []
    currtoken = ""
    intoken = False
    for ch in currline:
        if ch == '(':
            intoken = True
        elif ch == ')':
            tokens.append(currtoken)
            currtoken = ""
            intoken = False
        elif intoken:
            currtoken = currtoken + ch
        else:
            tokens.append(ch)
    #print tokens
    
    count = 0
    for word in words:
        count = count + 1
        for i, tok in enumerate(tokens):
            if not word[i] in tok:
                count = count - 1
                break
    #print count
    output.write(str(count) + "\n")

input.close()
output.close()
