#!/usr/bin/python

inf = open('input.txt','r')
outf = open('output.txt','w')

def find(root,V):
    if root['type']==1:
        if root['I']==V:
            return 0
        else:
            return -1
    
    lr = [find(root['left'],V),find(root['right'],V)]
    lr.sort()
    if lr[0] == lr[1] == -1:
        return -1
    if root['G']^V==1:
        if lr[0]==-1:
            return lr[1]
        return lr[0]
    else:
        if lr[0]==-1:
            if root['C']:
                return lr[1]+1
            else:
                return -1
        if root['C']:
            return min([lr[0]+1,lr[0]+lr[1]])
        else:
            return lr[0]+lr[1]

N = int(inf.readline())
for i in xrange(N):
    M,V = map(int,inf.readline().split(' '))
    root = {}
    line = [root]
    new_line = []
    for j in xrange((M-1)/2):
        G,C = map(int,inf.readline().split(' '))
        cur = line[0]
        line = line[1:]
        left = {}
        right = {}
        cur.update({'type':0,'G':G,'C':C,'left':left,'right':right})
        new_line.extend([left,right])
        if not line:
            line = new_line
            new_line = []

    for j in xrange((M+1)/2):
        I = int(inf.readline())
        cur = line[0]
        line = line[1:]
        cur.update({'type':1,'I':I})
        if not line:
            line = new_line
            new_line = []
    res = find(root,V)
    if res == -1:
        outf.write("Case #%d: IMPOSSIBLE\n"%(i+1,))
    else:
        outf.write("Case #%d: %d\n"%(i+1,res))
        
