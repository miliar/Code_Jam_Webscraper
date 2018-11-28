import sys

counter = 0
class Folder:
    def __init__(self, parent, name):
        global counter
        self.parent = parent
        self.name = name
        self.cildren = {}
        counter +=1
    
    def add(self, segments):
        if  not len(segments):
            return
        h = segments[0]
        tail = segments[1:]
        if h in self.cildren:
            self.cildren[h].add(tail)
        else:
            next = Folder(self, h)
            self.cildren[h] = next
            next.add(tail)

def main():
    inFile = open(sys.argv[1], 'rt')
    outFile = open(inFile.name.replace('.in', '.out'), 'wt')
#    outFile = sys.__stdout__
    T = int(inFile.readline())
    for t in xrange(1,T+1):
        N,M = map(int, inFile.readline().strip().split(' '))
        root = Folder(None, '')
        global counter
        for i in xrange(N):
            root.add(inFile.readline().strip()[1:].split('/'))
        counter = 0    
        for i in xrange(M):
            root.add(inFile.readline().strip()[1:].split('/'))
        outFile.write('Case #%d: %d\n' % (t, counter))
    outFile.close()
        

if __name__ == '__main__':
    main()
