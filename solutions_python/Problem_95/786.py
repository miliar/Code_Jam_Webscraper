table = {'a': 'y', 'b': 'h', 'c': 'e', 'd': 's', 'e': 'o', 'f': 'c', 'g': 'v', 'h': 'x', 'i': 'd', 'j': 'u', 'k': 'i', 'l': 'g', 'm': 'l', 'n': 'b', 'o': 'k', 'p': 'r', 'q': 'z', 'r': 't', 's': 'n', 't': 'w', 'u': 'j', 'v': 'p', 'w': 'f', 'x': 'm', 'y': 'a', 'z': 'q', ' ': ' ', '\n': '\n'}
inp = open('A-small-attempt1.in', 'r')
out = open('A-small-attempt1.out', 'w')
test = int(inp.readline())
for i in range(1, test+1):
    data = inp.readline()
    out.write("Case #%d: %s" %(i, ''.join([table[char] for char in data])))
