class Tree:
    def __init__(self):
        self.prob = 0
        self.feature = None
        self.pres = None
        self.abs = None
    def calc(self, prob, features):
        prob *= self.prob
        if self.feature is None:
            return prob
        if self.feature in features:
            return self.pres.calc(prob, features)
        else:
            return self.abs.calc(prob, features)
    def read(self, lines):
        self.prob = float(lines[1])
        if lines[2] == ")":
            return lines[3:]
        self.feature = lines[2]
        self.pres = Tree()
        lines = self.pres.read(lines[3:])
        self.abs = Tree()
        lines = self.abs.read(lines)
        return lines[1:]

#Templates:
# [int(x) for x in infile.readline().split()]

with open("A.in") as infile:
    with open("A.out",mode="wt") as outfile:
        cases = int(infile.readline())
        for ncase in range(cases):
            lines = "".join([infile.readline().strip() for i in range(int(infile.readline()))])
            lines = [x.strip() for x in lines.replace("("," ( ").replace(")"," ) ").split()]
            tree = Tree()
            tree.read(lines)
            nobj = int(infile.readline())
            outfile.write("Case #{nc}:\n".format(nc=ncase+1))
            for i in range(nobj):
                features = set(infile.readline().split()[2:])
                outfile.write("{prob:.7f}\n".format(prob=tree.calc(1.0, features)))
print("Ready")
