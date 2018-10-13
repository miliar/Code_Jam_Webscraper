import sys
import re
from pprint import pprint
input=sys.stdin

def parse_above(s):
    return s.split()[2:]

def parse_tree(d):
    d=''.join([x.strip() for x in d])
    d=re.sub('\(','[',d)
    d=re.sub('\)',']',d)
    d=re.sub('\]','],',d)
    d=re.sub('([a-z]+)',',\"\\1\",',d)
    s='p=%s' % d[:-1]
    p=eval(d)
    #d=re.sub('\[ ',',[',d)
    #pprint(p)
    return p

def peval(tree,above):
    p=1
    tree=tree[0]
    #pprint(tree)
    #pprint(above)
    while True:
        #print len(tree)
        if len(tree)==1:
            p=p*float(tree[0])
            break
        else:
            p=p*float(tree[0])
            if tree[1] in above:
                tree=tree[2]
            else:
                tree=tree[3]
    return p

T=int(input.readline())
for i in xrange(1,T+1):
    L=int(input.readline())
    tree=[]
    for l in xrange(L):
        tree.append(re.sub('\n','',input.readline()))
    tree=parse_tree(tree)
    A=int(input.readline())
    above=[]
    for a in xrange(A):
        above.append(re.sub('\n','',input.readline()))
    above=map(parse_above,above)
    
    #print tree
    #print above
    print 'Case #%s:' % i
    for a in xrange(len(above)):
        p=str(1+peval(tree,above[a]))
        if len(p)>9:
            p=p[:9]
        if len(p)<9:
            p=p+'0'*(9-len(p))
        if p[0]=='1':
            p=re.sub('^1','0',p)
        if p[0]=='2':
            p=re.sub('^2','1',p)

        print p
