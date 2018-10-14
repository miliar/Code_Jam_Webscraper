import Queue
class Key(object):
    def __init__(self, start,end):
        self.start = start
        self.end = end
        self.length = end-start+1
    def __cmp__(self,other):
        if self.length > other.length:
            return -1
        elif self.length < other.length:
            return 1
        elif self.start < other.start:
            return -1
        elif self.start > other.start:
            return 1
        else:
            return 0
def solve(N,K):
    pq = Queue.PriorityQueue()
    k = Key(1,N)
    pq.put(k)
    def find_pos(start,end):
        length = end - start + 1
        if length % 2 == 1:
            return [(start,start+(length-1)/2-1),(start+(length-1)/2+1,end)]
        else:
            return [(start,start+length/2-2),(start+length/2,end)]
    for i in range(K-1):
        interval = pq.get()
        res = find_pos(interval.start,interval.end)
        for c in res:
            p = Key(c[0],c[1])
            pq.put(p)
    final = pq.get()
    rr = find_pos(final.start,final.end)
    ls_r = rr[0]
    rs_r = rr[1]
    ls = ls_r[1]-ls_r[0]+1
    rs = rs_r[1]-rs_r[0]+1
    return (max(ls,rs),min(ls,rs))
"""
N = 10**6
K = 10**6
print solve(N,K)
"""

def readFile(path):
    with open(path, "rt") as f:
        return f.read()

def writeFile(path, contents):
    with open(path, "wt") as f:
        f.write(contents)

contentsRead = readFile("C-small-1-attempt0.in.txt")
contentsToWrite = ""
count = 1
for c in (contentsRead.split("\n")[1:-1]):
    N = c.split(" ")[0]
    K = c.split(" ")[1]
    res = solve(int(N),int(K))
    contentsToWrite += "Case #%d: " % count
    contentsToWrite += "%d %d" % res
    contentsToWrite += "\n"
    count+=1

writeFile("out.txt",contentsToWrite)


        
