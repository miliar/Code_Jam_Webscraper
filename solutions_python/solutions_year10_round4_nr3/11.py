from unionfind import *

class Rect:
    def __init__(self,l):
        self.x1=l[0]
        self.y1=l[1]
        self.x2=l[2]
        self.y2=l[3]

    def colliderect(self,r2):
        r1=self
        if r1.y2 < r2.y1-1: return False
        if r2.y2 < r1.y1-1: return False
        if r1.x2 < r2.x1-1: return False
        if r2.x2 < r1.x1-1: return False
        return True
        
def xl(l):
    return xrange(len(l))

def newr(l):
    return Rect(l)
    #return Rect(l[0],l[1],l[2]-l[0]+2,l[3]-l[1]+2)


debug=False
#debug=True
for case in range(input()):
    print "Case #"+str(case+1)+":",
    R=input()
    uf=UnionFind()
    rects=[]
    for i in xrange(R):
        newrect=newr(map(int,raw_input().split()))
        rects.append(newrect)
    #uf.insert_objects(rects)
    uf.insert_objects(range(R))
    for i in xrange(R):
        for j in xrange(R):
            if rects[i].colliderect(rects[j]):
                uf.union(i,j)
    if debug:
        print rects
        print uf.allsets()
    times=[]
    for l in uf.allsets().values():
        if l:
            rl=[rects[i] for i in l]
            maxx=max(r.x2 for r in rl)
            maxy=max(r.y2 for r in rl)
            if debug: print maxx,maxy
            times.append(max(maxx-r.x1+maxy-r.y1 for r in rl))
    print max(times)+1
