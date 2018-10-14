# coding: utf-8

cnt = 0
mode = 0
def addcnt():
    global cnt
    #print "addcnt -> "
    if mode == 1:
        #print "mkdir"
        cnt += 1

class Node(object):
    def __init__(self, label):
        self.label = label
        self.lst = []
    def mkdir(self, p):
        i = self.index(p[0])
        l = len(p)
        #print i,l,p
        if i != -1 and l == 1:
            #print "exists and len 1"
            pass
        elif i != -1 and l > 1:
            #print "exists and len > 1"
            node = Node(p[0])
            self.lst.append(node)
            self.lst[i].mkdir(p[1:])
        elif i == -1 and l == 1:
            #print "not exists and len 1"
            addcnt()
            node = Node(p[0])
            self.lst.append(node)
        elif i == -1 and l > 1:
            #print "not exists and len > 1"
            addcnt()
            node = Node(p[0])
            self.lst.append(node)
            node.mkdir(p[1:])
    def index(self, p):
        for i,n in enumerate(self.lst):
            if n.label == p:
                return i
        return -1

def main():
    global cnt,mode
    for t in xrange(input()):
        n,m = map(int, raw_input().split(" "))

        cnt,mode = 0,0
        root = Node("")
        for i in xrange(n):
            path = raw_input().split("/")[1:]
            root.mkdir(path)
        mode = 1
        for i in xrange(m):
            path = raw_input().split("/")[1:]
            root.mkdir(path)
        print "Case #%d: %d" % (t+1, cnt)

if __name__ == '__main__':
    main()
