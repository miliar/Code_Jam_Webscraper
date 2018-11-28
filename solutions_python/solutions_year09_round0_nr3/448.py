import os
import sys
msg = "welcome to code jam"

class Node(object):
    def __init__(self):
        self.char = ''
        self.pos = 0
        self.nodes = []
        self.index = -1;
        
    
def generateTree(char,pos,index,s):
    t = 0
    if index+2>len(msg):
        return 1 
    ch = msg[index+1]
    pos = pos+1
    while pos < len(s):
        if s[pos] == ch:
           t = t + generateTree(s[pos],pos,index+1,s)
           if len(str(t)) > 4:
               break
        pos=pos+1   
    return t

f = file("d:\\b.txt")

cases = int(f.readline())
for q in range(0,cases):
    total = 0
    s = f.readline()
    root = Node()
    for i in range(0,len(msg)):
        for z in range(0,len(s)):
            if s[z] == msg[i]:
               n = Node()
               n.char = s[z]
               n.pos = z
               n.index = i
               root.nodes.append(n)
        for nd in root.nodes:
            total = total + generateTree(nd.char,nd.pos,nd.index,s)
        break
    while len(str(total)) > 4:
        total = total - 1
    rem = 4 - len(str(total))    
    print "Case #" + str(q+1) + ": " + '0'*rem + str(total)
f.close()    
    