transmap = {' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q'}
with open("A-small-attempt0.in") as infile:
    numtimes = int(infile.readline())
    for x in range(numtimes):
        line = infile.readline().strip();
        newstr = ""
        for ch in line:
            newstr += transmap[ch]
        print("Case #%d: %s" %(x + 1, newstr))
