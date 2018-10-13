newdict={' ': ' ', 'z': 'q', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm'}
inp = raw_input("input: ")
lines = inp.split("\n")
for x in xrange(1,len(lines)):
    newString = ""
    for letter in lines[x]:
        newString += newdict[letter]
    print "Case #" + str(x) + ": " + newString
