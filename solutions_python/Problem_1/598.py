
engines = []

class Solve:
    
    def __init__(self, requests):
        self.requests = requests
        print "engines", engines
        print "requests", self.requests

    def run(self):
#        self.search([])
#        for candidate in breadth_first([], children):
#            if self.solutionWorks(candidate):
#                break
            solution = []
            while True:
                maxEng = engines[0]
                if not maxEng in self.requests:
                    solution.append(maxEng)
                    break
                else:
                    maxIndex = self.requests.index(maxEng)

                for eng in engines[1:] :
                    if not eng in self.requests:
                        maxEng = eng
                        maxIndex = len(self.requests)
                        break
                    if self.requests.index(eng) > maxIndex:
                        maxEng = eng
                        maxIndex = self.requests.index(maxEng)
                solution.append(maxEng)
                self.requests = self.requests[maxIndex:]
                if len(self.requests) == 0:
                    break
            print "solution", solution
            out( str(len(solution) -1) + "\n")

    def search(self, candidate):
        for eng in self.engines:
            candidate.append(eng)
            if self.solutionWorks(candidate):
                return True
            candidate.pop()
        for eng in self.engines:
            candidate.append(eng)
            if self.search(candidate):
                return True
            candidate.pop()

    def solutionWorks(self, candidate):
        if not candidate:
            return False
        can = list(candidate)
        eng = can.pop(0)
        for req in self.requests:
            if req == eng:
                while can and eng == req:
                    eng = can.pop(0)
                if eng == req:
#                    print "Solution does not work", candidate
                    return False
        print "Solution found", candidate
        out( str( len(candidate) - 1) + "\n")
        return True

def out(s):
    print s,
    fOut.write(s)

def children(node):
    children = []
    for eng in engines:
        children.append(node + [eng])
    return children
    
def breadth_first(tree,children=iter):
    """Traverse the nodes of a tree in breadth-first order.
    The first argument should be the tree root; children
    should be a function taking as argument a tree node and
    returning an iterator of the node's children.
    """
    yield tree
    last = tree
    for node in breadth_first(tree,children):
        for child in children(node):
            yield child
            last = child
        if last == node:
            return

if __name__ == "__main__":
    name = "A-large"
    fIn = open(name + '.in','r')
    fOut = open(name + '.out','w')
    cases = int(fIn.readline().rstrip())
    for caseNumber in range(cases):
        engines = []
        requests = []
        
        numEngines = int(fIn.readline().rstrip())
        for i in range(numEngines):
            name = fIn.readline().rstrip()
            engines.append(name)

        numRequests = int(fIn.readline().rstrip())
        for i in range(numRequests):
            req = fIn.readline().rstrip()
            requests.append(req)

        out("Case #%d: " % (caseNumber + 1))
        Solve(requests).run()
    fIn.close()
    fOut.close()