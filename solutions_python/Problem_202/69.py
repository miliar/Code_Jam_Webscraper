import numpy as np

# Hopcroft-Karp bipartite max-cardinality matching and max independent set
# David Eppstein, UC Irvine, 27 Apr 2002

def bipartiteMatch(graph):
    '''Find maximum cardinality matching of a bipartite graph (U,V,E).
    The input format is a dictionary mapping members of U to a list
    of their neighbors in V.  The output is a triple (M,A,B) where M is a
    dictionary mapping members of V to their matches in U, A is the part
    of the maximum independent set in U, and B is the part of the MIS in V.
    The same object may occur in both U and V, and is treated as two
    distinct vertices if this happens.'''
    
    # initialize greedy matching (redundant, but faster than full search)
    matching = {}
    for u in graph:
        for v in graph[u]:
            if v not in matching:
                matching[v] = u
                break
    
    while 1:
        # structure residual graph into layers
        # pred[u] gives the neighbor in the previous layer for u in U
        # preds[v] gives a list of neighbors in the previous layer for v in V
        # unmatched gives a list of unmatched vertices in final layer of V,
        # and is also used as a flag value for pred[u] when u is in the first layer
        preds = {}
        unmatched = []
        pred = dict([(u,unmatched) for u in graph])
        for v in matching:
            del pred[matching[v]]
        layer = list(pred)
        
        # repeatedly extend layering structure by another pair of layers
        while layer and not unmatched:
            newLayer = {}
            for u in layer:
                for v in graph[u]:
                    if v not in preds:
                        newLayer.setdefault(v,[]).append(u)
            layer = []
            for v in newLayer:
                preds[v] = newLayer[v]
                if v in matching:
                    layer.append(matching[v])
                    pred[matching[v]] = v
                else:
                    unmatched.append(v)
        
        # did we finish layering without finding any alternating paths?
        if not unmatched:
            unlayered = {}
            for u in graph:
                for v in graph[u]:
                    if v not in preds:
                        unlayered[v] = None
            return (matching,list(pred),list(unlayered))

        # recursively search backward through layers to find alternating paths
        # recursion returns true if found path, false otherwise
        def recurse(v):
            if v in preds:
                L = preds[v]
                del preds[v]
                for u in L:
                    if u in pred:
                        pu = pred[u]
                        del pred[u]
                        if pu is unmatched or recurse(pu):
                            matching[v] = u
                            return 1
            return 0

        for v in unmatched: recurse(v)


def solve(n, crossList, plusList):
    
    ## vertices are constraints
    ## the edges are (x,y) points -- that are at the intersection of two constraints
    
    ## from constraint name --> list of (x,y) on that constraint
    vHor = {}; 
    vVer = {};
    vDiag1 = {};
    vDiag2 = {};
    
    fromXYToVHorName = {};
    fromXYToVVerName = {};
    fromXYToVDiag1Name = {};
    fromXYToVDiag2Name = {};

    fromVHorVVerNamesToXY = {};
    fromVDiag1VDiag2NamesToXY = {};

    for x in range(1,n+1):
        for y in range(1,n+1):
            
            if(x not in vHor):
                vHor[x] = [];
            if(y not in vVer):
                vVer[y] = [];
            if(x-y not in vDiag1):
                vDiag1[x-y] = [];
            if(x+y not in vDiag2):
                vDiag2[x+y] = [];
                
            
            vHor[x].append([x,y]);
            vVer[y].append([x,y]);
            vDiag1[x-y].append([x,y]);
            vDiag2[x+y].append([x,y]);

            fromXYToVHorName[(x,y)] = x;
            fromXYToVVerName[(x,y)] = y;
            fromXYToVDiag1Name[(x,y)] = x-y;
            fromXYToVDiag2Name[(x,y)] = x+y;
    
            fromVHorVVerNamesToXY[(x,y)] = [x,y];
            fromVDiag1VDiag2NamesToXY[(x-y,x+y)] = [x,y];
    
    for (x,y) in crossList:
        del vHor[fromXYToVHorName[(x,y)]];
        del vVer[fromXYToVVerName[(x,y)]];

    for (x,y) in plusList:
        del vDiag1[fromXYToVDiag1Name[(x,y)]];
        del vDiag2[fromXYToVDiag2Name[(x,y)]];

    ## now add edges 
    gCross = {};
    for vh in vHor:
        gCross[vh] = [];
    
    gPlus = {};
    for vd1 in vDiag1:
        gPlus[vd1] = [];
            
    for x in range(1,n+1):
        for y in range(1,n+1):
            vh = fromXYToVHorName[(x,y)];
            vv = fromXYToVVerName[(x,y)];
            
            if((vh in vHor) and (vv in vVer)):
                gCross[vh].append(vv);
            
            vd1 = fromXYToVDiag1Name[(x,y)];
            vd2 = fromXYToVDiag2Name[(x,y)];
            
            if((vd1 in vDiag1) and (vd2 in vDiag2)):
                gPlus[vd1].append(vd2);
            
            
    mCross, a, b = bipartiteMatch(gCross);
    
    mPlus, a, b = bipartiteMatch(gPlus);
    
    score = len(crossList)+len(plusList)
    
    oldCross = set([str(x)+' '+str(y) for (x,y) in crossList]);
    oldPlus = set([str(x)+' '+str(y) for (x,y) in plusList]);
    
    newCross = set(oldCross);
    newPlus = set(oldPlus);

    oldCir = oldCross.intersection(oldPlus);
    oldCross = oldCross.difference(oldCir);
    oldPlus = oldPlus.difference(oldCir);
    
    for vv in mCross:
        vh = mCross[vv];
        [x,y] = fromVHorVVerNamesToXY[(vh,vv)];
        newCross.add(str(x)+" "+str(y));
        score+=1;

    for vd2 in mPlus:
        vd1 = mPlus[vd2];
        [x,y] = fromVDiag1VDiag2NamesToXY[(vd1,vd2)];
        newPlus.add(str(x)+" "+str(y));
        score+=1;
    
    newCir = newCross.intersection(newPlus);
    newCross = newCross.difference(newCir);
    newPlus = newPlus.difference(newCir);

    out="";
    total_size = 0;
    for c in newCir.difference(oldCir):
        out+='o '+c+"\n";
        total_size+=1;
    for c in newPlus.difference(oldPlus):
        out+='+ '+c+"\n";
        total_size+=1;
    for c in newCross.difference(oldCross):
        out+='x '+c+"\n";
        total_size+=1;

    out = str(score) + " " + str(total_size) +"\n"+out;

#     print 'oldCir', oldCir
#     print 'newCir', newCir

#     str1 = '';
#     for i in range(1,n+1):
#         for j in range(1,n+1):
#             if str(i)+' '+str(j) in newCross:
#                 str1+='x';
#             elif str(i)+' '+str(j) in newPlus:
#                 str1+='+';
#             elif str(i)+' '+str(j) in newCir:
#                 str1+='o';
#             else:
#                 str1+=' ';
#         str1+='\n';
#     print str1

    return out;
    
# f = file('/home/jabot/Downloads/2017_q4_sample.in');
# fout = file('/home/jabot/Downloads/2017_q4_sample.out','w');

f = file('/home/jabot/Downloads/D-large.in');
fout = file('/home/jabot/Downloads/D-large.out','w');

lines = f.readlines();
print lines
T = int(lines[0]);

cnt=0;
li=1;

while cnt<T:
    [n,m] = lines[li].split(' ');
    print '---', n
    m = int(m);
    n = int(n);
    crossList = [];
    plusList = [];
    for e in lines[li+1:li+m+1]:
        #print e.strip()
        [s, x, y] = e.strip().split(' ');
        if(s=='x' or s=='o'):
            crossList.append((int(x),int(y)));
        if(s=='+' or s=='o'):
            plusList.append((int(x),int(y)));
 
    li+=m+1;
    cnt+=1;
 
#     print crossList, plusList
   
    out = solve(n, crossList, plusList);

#     print out;
    
    fout.write('Case #'+str(cnt)+": "+out.strip()+"\n");

fout.close();

