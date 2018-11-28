
import copy
import Queue

def array_input():
    NM = raw_input().split()
    return [ int(i) for i in NM]

def int_input():
    return int(raw_input())
    
class Log():
    def __init__(self, debug=False):
        self.debug = debug

    def info(self, fmt, *args):
        if self.debug:
            print fmt % args

    
            
def solve():
    stn = raw_input()
    st,n = stn.split()
    n = int(n)
    v = []
    ca = []
    log.info("%s %s", st,n)
    for c in st:
        if c in ['a','e','i','o','u']:
            v.append(0)
        else:
            v.append(1)

    count = 0
    q = Queue.Queue(n)
    last = 0
    isset = 0
    for i in range(0, len(st)):
        log.info(" %d len %d vi %d",i, q.qsize(), v[i])
        if q.qsize() < n-1:
            q.put(v[i])
            count += v[i]        
            if v[i] == 0:
                q = Queue.Queue(n)
                count = 0
            ca.append(0)
            continue
        
        q.put(v[i])
        count += v[i]
        
        if count == n:
            ca.append(n)
        else:
            ca.append(0)
        
        count -= q.get()
        
            
    log.info( "count %d %s",count, `ca`)            
    count = 0
    l = len(st)
    last_n = -1
    
    log.info("%s %s",v, ca)
    for i in range(len(st)-1, n-2, -1):
        if ca[i] == n:
            last_n = i
        
        if last_n == -1:
            continue
        count += (l - last_n)

    return  count
    
log = Log(0)
if __name__ == '__main__':
    case = int_input()
    for i in range(1, case+1):
        ans = solve()
        print "Case #%d: %s"%(i, ans)