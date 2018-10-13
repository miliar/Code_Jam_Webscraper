'''
Created on 13/04/2013

@author: David Llorens
'''
import sys
import time

def mihash(s):
    return hash(tuple(s[0])) ^ hash(tuple(s[1]))

class ChestStateSpace:
    def __init__(self, keys, chests):
        self.keys, self.chests = keys, chests
        self.N = len(self.chests)
        
    def initial_states(self):
        yield [keys, [False]*self.N, self.N]
    
    def is_final(self, s):
        return s[2] == 0
    
    def decisions(self, s):
        for d in range(self.N):
            if s[1][d]==False and s[0][self.chests[d][0]]>0: yield d
                
    def decide(self, s, d):
        keys = s[0]
        chest = self.chests[d]
        keys[chest[0]] -= 1
        cd = chest[1]
        for i in range(len(cd)):
            keys[i] += cd[i]
        s[1][d] = True
        s[2] -= 1
        return s
    
    def undo(self, s, d):
        keys = s[0]
        chest = self.chests[d]
        keys[chest[0]] += 1
        cd = chest[1]
        for i in range(len(cd)):
            keys[i] -= cd[i]
        s[1][d] = False
        s[2] += 1
        return s

class BacktrackingEnumerator:
    def enumerate(self, space):
        def backtracking(state):
            if space.is_final(state): 
                yield tuple(decisions)
            seen.add(mihash(state))
            for decision in space.decisions(state):
                decisions.append(decision)
                successor = space.decide(state, decision)
                if mihash(successor) not in seen:
                    for result in backtracking(successor): 
                        yield result
                state = space.undo(successor, decision)
                decisions.pop()
        
        decisions = []
        seen = set()
        
        for initial in space.initial_states():
            #print(mihash(initial))
            for result in backtracking(initial): 
                yield result
    
    def first(self, space: "IForwardStateSpace") -> "Solution or None":
        return next(self.enumerate(space), None)
        
res = []
fn = "d-small.in"
fn = "/Users/david/Downloads/D-small-attempt0.in" 
fn = sys.argv[1] 
f = open(fn, "r")
T = int(f.readline().strip())
start = time.clock()

MAXKEY=20
#print(T)
fout = open("resD.txt", "w")
for t in range(T):
    
    kk = [int(e) for e in f.readline().strip().split()]
    K, N = kk[0], kk[1]
    
    keys = [0]*MAXKEY
    for key in [int(e)-1 for e in f.readline().strip().split()]:
        if key>=0 and key<len(keys):
            keys[key] += 1
    chests=[0]*N
    for nlin in range(N):
        chests[nlin] = [0,[0]*MAXKEY]
        nums = [int(e) for e in f.readline().strip().split()]
        chests[nlin][0] = nums[0]-1
        #print("kk",nums)
        for ii in range(nums[1]):
            chests[nlin][1][nums[2+ii]-1] += 1

    #print(N, sum(sum(c[1]) for c in chests)+sum(keys))
    #if t==1: continue
    #print(keys,chests)
    #print("K:{0}, N: {1}".format(K, N))
    
    space = ChestStateSpace(keys, chests)
    sol = BacktrackingEnumerator().first(space)
    if sol!=None:
        cad = "Case #{0}: {1}".format(t+1, ' '.join([str(s+1) for s in sol]))
    else:
        cad = "Case #{0}: IMPOSSIBLE".format(t+1)
    fout.write(cad+"\n")
    print(cad)
    

fout.close()
elapsed = (time.clock() - start)
print(elapsed)
print("END")