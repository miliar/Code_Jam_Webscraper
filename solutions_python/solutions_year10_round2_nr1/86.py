import sys;
sys.setrecursionlimit(100000);

def doProb(fname, ofname):
    #do problem A given a file name
    f = open(fname, 'r');
    of = open(ofname, 'w');
    T = int(f.readline());
    output = [];
    for i in range(1,T+1):
        [N,M] = [int(x) for x in f.readline().split()];
        root = [''];
        addpaths(root,[f.readline().strip() for i in range(1,N+1)]);
        tot = addpaths(root, [f.readline().strip() for i in range(1,M+1)]);    
        output.append('Case #' + str(i) + ': ' + str(tot)+'\n');
    f.close();  
    
    of.writelines(output);
    of.close();

def addpaths(T,s):    
    tot = 0;
    for p in s:        
        path = p[1:].split('/');
        tot += addnode(T, path);
    return tot;

def addnode(T, node):
    if(node == []):
        return 0;    
    for L in T[1:]:
        if(L[0]==node[0]):
            return addnode(L,node[1:]);
    T.append(nest(node));
    return len(node);
    
def nest(x):
    if(len(x)==1):
        return x;
    return [x[0],nest(x[1:])]
