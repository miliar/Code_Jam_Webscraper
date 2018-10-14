class Tree:
    def __init__(self, name=""):
        self.name = name
        self.kids = {}
    
    def insert(self, seq):
        if len(seq) == 0: return 0

        k = seq[0]
        seq = seq[1:]
        if k == "": 
            return self.insert(seq)

        if k not in self.kids:
            self.kids[k] = Tree(k)
            return 1 + self.kids[k].insert(seq)
        else:
            return self.kids[k].insert(seq)

def count():
    N, M = [ int(i) for i in input().split() ]
    t = Tree()
    for _ in range(N):
        t.insert(input().split("/"))

    total = 0
    for _ in range(M):
        total += t.insert(input().split("/"))

    return total
    

for case in range(int(input())):
    print("Case #" + str(case+1) + ": " + str(count()))
