import re
from numarray import *

class OBJ:pass
N=int(raw_input())

def walk(node, p, features):
    p*=node.prob
    if node.feature in features:
        p=walk(node.children[0],p,features)
    else:
        try: p=walk(node.children[1],p,features)
        except: pass
    
    return p
    
for case_no in range(1,N+1):
    L=int(raw_input())    
    tree=''.join([raw_input() for i in range(L)])    
    tree=tree.replace("(", " ( ").replace(")", " ) ")
    
    TREE=OBJ()
    TREE.children=[]
    TREE.parent=None
    NODE=TREE
    state=0
    for token in tree.split():
        if token=="(":                        
            node=OBJ()
            node.children=[]
            node.parent=NODE
            NODE.children.append(node)
            NODE=node
        elif token==")":
            NODE=NODE.parent
        else:
            try:
                f=float(token)
                NODE.feature=''
                NODE.prob=f
            except:
                NODE.feature=token
    
    print "Case #%d:" % case_no
    
    A=int(raw_input())    
    for i in range(A):
        features=filter(bool, raw_input().split())
        animal=features.pop(0)
        features.pop(0)
        
        p=walk(TREE.children[0], 1.0, features)
        
        print "%.06f" % p
