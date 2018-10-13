'''
Created on May 22, 2010

@author: francesccampoyflores
'''

import sys

class Folder:
    def __init__(self):
        self.children = {}
    
    def createFolder(self, path):
        #print "createFolder : "+str(path)
        
        if len(path) == 0:
            return 0
        
        child = path[0]
        if child in self.children:
            #print "Entering into "+child
            return self.children[child].createFolder(path[1:])
        else:
            #print "Creating and Entering into "+child
            self.children[child] = Folder()
            return self.children[child].createFolder(path[1:]) + 1

if __name__ == '__main__':
    input = open(sys.argv[1],'r')
    output = open(sys.argv[2], 'w')
    
    
    T = int(input.readline())
    
    for t in range(1, T+1):
        N, M = map(int, input.readline().split())
        
        root = Folder()
        
        for n in range(N):
            path = input.readline()[:-1].split("/")[1:]
            root.createFolder(path)
        
        result = 0
        for m in range(M):
            path = input.readline()[:-1].split("/")[1:]
            result += root.createFolder(path)
        
        output.write("Case #%d: %d\n"%(t, result))