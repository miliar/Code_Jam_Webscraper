import math
import queue
import time

class Timer(object):
    def __init__(self, name=None):
        self.name = name

    def __enter__(self):
        self.tstart = time.time()

    def __exit__(self, type, value, traceback):
        if self.name:
            print('[%s]' % self.name)
        print('Elapsed: %s' % (time.time() - self.tstart))

tc = 0

def takeAStall(available_segments):
    next_segment = available_segments.get()
    middle = (next_segment[0]+next_segment[1])/2.0
    p = None
    if math.floor(middle)==middle:
        p=int(middle)
        available_segments.put([next_segment[0],p])
        available_segments.put([p,next_segment[1]])
    else:
        p=int(middle)
        available_segments.put([p,next_segment[1]])
        available_segments.put([next_segment[0],p])
    return p

def getNextStats(available_segments):
    next_segment = available_segments.get()
    middle = (next_segment[0]+next_segment[1])/2.0
    p = int(middle)
    d1 = abs(next_segment[0]-p)-1
    d2 = abs(next_segment[1]-p)-1
    return max(d1,d2),min(d1,d2)

def distibute(N,K):
    available_segments=queue.Queue()
    available_segments.put([-1,N])
    for j in range(K-1):
        p = takeAStall(available_segments)
    return available_segments

def computeResult(N,K):
    ops = [int(x) for x in str(bin(K))[2:]]
    b=N
    c=0
    for i in range(len(ops)):
        b=(b-1.0)/2
        c=c+2**i
    nStage = 2**(len(ops)-1)
    naffected = 2*nStage*(b-math.floor(b))
    assert(int(naffected)==naffected)
    place1 = K-c+nStage
    place2 = place1+nStage
    cv = math.ceil(b) if place1<=naffected else math.floor(b)
    fv = math.ceil(b) if place2<=naffected else math.floor(b)
    return cv,fv
    # a = N
    # if len(ops)>1:
    #     a = math.ceil((a-1.0)/2)
    # for i in range(1,len(ops)-1):
    #     if ops[i]:
    #         a=math.floor((a-1.0)/2)
    #     else:
    #         a=math.ceil((a-1.0)/2)
    # a=max(a,1)
    # a=(a-1.0)/2
    # print(b,nStage,affected,K-c+nStage)
    # return math.ceil(a),math.floor(a)

def sanityCheck(N,K):
    pmi,pma = N,N
    for j in range(1,K):
        cmi,cma = computeResult(N,j)
        if not ((pmi>=cmi) and (pma>=cma)):
            print(j,pmi,pma,cmi,cma)
            assert(((pmi>=cmi) and (pma>=cma)))
        pmi,pma = cmi,cma

t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    N = [int(x) for x in input().split()]
    K = N[1]
    N = N[0]
    # sanityCheck(N,K)
        # with Timer('new'):
        #     for j in range(10,0,-1):
    ma,mi = computeResult(N,K)
        #         print(K-j,ma,mi)
        # with Timer('old'):
    # mao,mio = getNextStats(distibute(N,K))
    # print("Case #{}: {} {}; {} {}".format(i, ma, mi, mao, mio))
    print("Case #{}: {} {}".format(i, ma, mi))
        # assert(ma==mao)
        # assert(mi==mio)

    # check out .format's specification for more formatting options
