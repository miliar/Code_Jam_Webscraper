inp = open("d:\\incoming\\a-large.in", "r")
#inp = open("d:\\incoming\\a-small-attempt0.in", "r")
#inp = open("d:\\incoming\\a.in", "r")

outp = open(".\\a.out", "w")

class Node:
    def __init__(self):
        self.children = [None] * 27

    def add(self, s):
        if s == "": return
        first = ord(s[0]) - ord('a')
        if self.children[first] == None:
            self.children[first] = Node()
        self.children[first].add(s[1:])

    def count(self, s):
        if s == "": return 1
        ret = 0
        if s[0] == "(":
            idx = s.find(")")
            assert idx != -1
            cands = s[1:idx]
            nexts = s[idx+1:]            
        else:
            cands = s[0]
            nexts = s[1:]

        for char in cands:
            ch = ord(char) - ord('a')
            if self.children[ch] != None:
                ret += self.children[ch].count(nexts)
        return ret

l, d, n = map(int, inp.readline().split())

root = Node()
for i in xrange(d):
    root.add(inp.readline().strip())

for i in xrange(n):
    ret = "Case #%d: %d" % (i+1, root.count(inp.readline().strip()))
    print ret
    outp.write(ret + "\n")
    
outp.close()
