class Space:
    def __init__(self, length):
        self.minx = (length-1)//2
        self.maxx = length//2
        self.length = length
    def __lt__(self,other):
        return (self.minx > other.minx or 
            (self.minx == other.minx and self.maxx > other.maxx))
    def __eq__(self,other):
        return self.length == other.length
    def __hash__(self):
        return self.length

class SpaceHolder:
    def __init__(self,N):
        self.set = {Space(N):1}
    def add(self,space,num):
        if space in self.set:
            self.set[space] += num
        else:
            self.set[space] = num
    def min_num(self):
        return self.set[min(self.set)]
    def pop_min(self):
        m = min(self.set)
        n = self.set[m]
        del self.set[m]
        return m,n
    def is_last(self,k_left):
        return k_left <= self.min_num()

    
def get_last(N,K):
    sp = SpaceHolder(N)
    k_left = K
    while not sp.is_last(k_left):
        mspace,num = sp.pop_min()
        sp.add(Space(mspace.minx),num)
        sp.add(Space(mspace.maxx),num)
        k_left -= num
    mspacelast,_ = sp.pop_min()
    return mspacelast
    
T = int(input())
for case in range(T):
    vals = input().split()
    N,K = int(vals[0]),int(vals[1])
    
    last_space = get_last(N,K)
    
    
    #print(S)
    outstr = "Case #{}: {} {}".format(case+1,last_space.maxx,last_space.minx)
    print(outstr)
    