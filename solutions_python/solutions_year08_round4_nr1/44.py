import sys,os,glob

def changes(A, wantTrue, overrideChangable = False, isChanged = False, depth=0):
    if A.value is None:
        if A.isChangable and not overrideChangable:
            #~ print "trychanged-and-not",
            ret = min(changes(A, wantTrue, True, isChanged = False, depth=depth+1), 1+changes(A, wantTrue, True, isChanged = True, depth=depth+1))
        else:
            if (A.isAnd and not isChanged) or (not A.isAnd and isChanged):
                if wantTrue:
                    ret = changes(A.left, True, depth=depth+1) + changes(A.right, True, depth=depth+1)
                else:
                    ret = min(changes(A.left, False, depth=depth+1), changes(A.right, False, depth=depth+1))
            else: # or
                if wantTrue:
                    ret = min(changes(A.left, True, depth=depth+1),changes(A.right, True, depth=depth+1))
                else:
                    ret = changes(A.left, False, depth=depth+1) + changes(A.right, False, depth=depth+1)
    else:
        if A.value==wantTrue:
            ret = 0
        else:
            ret = 1000000000

    #~ print "  "*depth, A.id,"want", wantTrue, overrideChangable, isChanged, "returns",ret
    return ret

class Node:
    def __init__(self, id, isAnd, isChangable = None):
        self.id = id
        if isChangable is None:
            self.value = isAnd
        else:
            self.isAnd = isAnd
            self.isChangable = isChangable
            self.value = None
    def __str__(self):
        if self.value is None:
            return "%d L=%d R=%d"%(self.id,self.left.id, self.right.id)
        else:
            return "%d"%(self.id)

if __name__=='__main__':
    xxx = open(sys.argv[1]).readlines()

    #~ print xxx
    N = int(xxx.pop(0))
    #~ print T

    for i in range(N):
        temp = xxx.pop(0).split()
        M = int(temp[0])
        V = int(temp[1]) == 1
        numNode = -1
        nodes = []
        for j in range((M-1)/2):
            numNode+=1
            temp = xxx.pop(0).split()
            #~ print j,temp
            G = int(temp[0]) == 1
            C = int(temp[1]) == 1
            nodes.append(Node(numNode,G, C))
        for j in range((M+1)/2):
            numNode+=1
            I = int(xxx.pop(0)) == 1
            nodes.append(Node(numNode,I))
        rootNode = nodes[0]
        #~ print "//"
        for z,n in enumerate(nodes[1:]):
            nodeID = z+1
            isLeft = nodeID/2 == (nodeID-1)/2
            #~ print i,nodeID,(nodeID-1)/2,isLeft
            if isLeft:
                nodes[(nodeID-1)/2].left = n
            else:
                nodes[(nodeID-1)/2].right = n

        #~ for n in nodes:
            #~ print n

        ret = changes(rootNode, V)
        if ret >= 1000000000:
            ret = "IMPOSSIBLE"
        print "Case #%d: %s" % (i+1, ret)
        #~ print V

