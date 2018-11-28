file = open("A-large.in")

class Directory:
    def __init__(self, name):
        self.name = name
        self.children = {}
        
    def insert(self, path):
        if len(path) == 0:
            return 0
        
        if path[0] in self.children:
            return self.children[path[0]].insert(path[1:])
        else:
            child = Directory(path[0])
            self.children[path[0]] = child
            return 1 + child.insert(path[1:])
            
T = int(file.readline())
for t in xrange(T):
    (N, M) = map(int, file.readline().split(' '))
    
    root = Directory('')
    
    for n in xrange(N):
        path = file.readline().rstrip("\n").split('/')[1:]
        root.insert(path)
       
    y = 0 
    for m in xrange(M):
        path = file.readline().rstrip("\n").split('/')[1:]
        y += root.insert(path)

    print "Case #%i: %s" % (t+1, y)
