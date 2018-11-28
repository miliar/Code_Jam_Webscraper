class Snapper(object):
    """
    """
    
    def __init__(self, ):
        """
        """
        self.power = False
        self.state = False
    def toggle(self):
        self.state = not self.state

def toggle_snappers(snapperChain):
    """
    """
    for i in snapperChain:
        if i.power:
            i.toggle()

    for i in xrange(1, len(snapperChain)):
        if (snapperChain[i-1].power and snapperChain[i-1].state):
            snapperChain[i].power = True
        else:
            snapperChain[i].power = False
        



def run_case(n, k):
    snapperChain = []
    for i in xrange(n):
        snapperChain.append(Snapper())
    for i in xrange(k):
        snapperChain[0].power = True
        toggle_snappers(snapperChain)
    return 'ON' if snapperChain[-1].power and snapperChain[-1].state else 'OFF'
    
    
def read_input(file):
    """
    """
    outputFile = open('A-small.out', 'w')
    with open(file) as f:
        numCases = f.readline()
#        print 'Number of cases = %s' % numCases
        for n,line in enumerate(f):
            
            outputLine = 'Case #{0}: {1}'.format(n+1, run_case(*[int(i) for i in line.split()]))
            outputFile.write(outputLine + '\n')
#            print line

def main():
    read_input('A-small-attempt0.in')
    


if __name__ == '__main__':
    main()
