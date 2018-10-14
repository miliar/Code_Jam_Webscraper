add_count = 0

class Directory:
    def __init__(self, name):
        self.name = name
        self.children = {}

    def add_path(self, path):
        child = self.add_child(path[0])
        if len(path) > 1:
            child.add_path(path[1:])

    def add_child(self, name):
        global add_count
        if name not in self.children:
            self.children[name] = Directory(name)
            add_count += 1
            #print "add", name
        return self.children[name]

    
T = input()
for t in range(T):
    N, M = map(int, raw_input().split(" "))
    root = Directory("/")

    for n in range(N):
        root.add_path(raw_input()[1:].split("/"))
    #print "-----------"
    add_count = 0
    for m in range(M):
        root.add_path(raw_input()[1:].split("/"))

    print "Case #%d: %d" % (t+1, add_count)

    
                     
