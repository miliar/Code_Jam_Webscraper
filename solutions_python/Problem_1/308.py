from time import time
import psyco
psyco.full()

fin = open("universe_input.txt","r")
fout = open("universe_output.txt","w")
cases = int(fin.readline())


#data = [map(int,lines.split()) for lines in fin.readlines()]
#print data

def sort_by_nonconflict(current, position, engines, cases):
    d = {}
    for e in engines:
        d[e] = next_conflict(e, position, cases)
    
    return sort_by_value(d).remove(cases[position]).reverse()
    
def sort_by_value(d):
    """ Returns the keys of dictionary d sorted by their values """
    items=d.items()
    backitems=[ [v[1],v[0]] for v in items]
    backitems.sort()
    return [ backitems[i][1] for i in range(0,len(backitems))]


def next_conflict(current, position, cases):
    for indx in range(position,len(cases)):
        if cases[indx] == current:
            return indx

def search(current, position, engines, cases, depth):
    global max_depth
    if max_depth < depth:
        return -1
    sorted_engines = sort_by_nonconflict(current, position, engines, cases)
    next_pos = next_conflict(sorted_engines[-1], position, cases)
    if (next_pos == None):
        if max_depth > depth:
            max_depth = depth
        return 0
    
    #min([search(e,)
 
def minf(li, f):
    minval = f[li[0]]
    minindex = 0
    for i in range(1,len(li)):
        if f[li[i]] < minval:
            minval = f[li[i]]
            minindex = i
    return minindex
    
def dist(a,b):
    global engines
    minsteps = max(1, int((b-a)/(len(engines)-1)))
    return minsteps
    
def get_next_pos(index, engines, cases):
    engine_pos = {}
    subset = cases[index+1:]
    if index >= 0: 
        not_allowed = cases[index]
    else:
        not_allowed = None
    hit_not_allowed = False
    ind = index
    for c in subset:
        ind += 1
        if c == not_allowed:
            hit_not_allowed = True
        elif c not in engine_pos:
            engine_pos[c] = ind
    
    difference = len(engines)-len(engine_pos)
    print "diff:",difference
    print "na:",not_allowed
    print "nei:",engine_pos
    if difference >= 1 and not hit_not_allowed:
        pass
        #return -1 #finished
    if difference >= 2:
        return -1 #finished
    
    return engine_pos.values()
    
def astar(start, goal, engines, cases):
    closed = []
    open = [start]
    g_score = {}
    f_score = {}
    h_score = {}
    if goal == -1: 
        return 0
    g_score[start] = 0
    f_score[start] = dist(start, goal)
    while open:
        x_ind = minf(open, f_score)
        x = open[x_ind]
        print "current:",x
        if x == goal:
            return g_score[x]
        
        closed.append(open.pop(x_ind))
        
        neighbours = get_next_pos(x, engines, cases)
        if x == -1 and len(engines)>len(neighbours):
            return 0

        if neighbours == -1:
            return g_score[x]
        for n in neighbours:
            if n in closed:
                continue
            new_g = g_score[x] + 1
            new_g_better = False
            
            if n not in open:
                open.append(n)
                h_score[n] = dist(n, goal)
                new_g_better = True
            elif new_g < g_score[n]:
                new_g_better = True
            
            if new_g_better:
                g_score[n] = new_g
                f_score[n] = g_score[n] + h_score[n]
        
    

t0 = time()
for casenr in range(cases):
    print "CASE: ",(casenr+1)
    engine_count = int(fin.readline())
    engines = []
    for e in range(engine_count):
        engines.append(fin.readline().strip())
    
    case_count = int(fin.readline())
    cases = []
    for c in range(case_count):
        cases.append(fin.readline().strip())
    
    worst_solution = int(len(cases)/(len(engines)-1))
    total_steps = len(cases)/len(engines)
    print "worst:",total_steps
    

    aa = astar(-1, len(cases)-1, engines, cases)
    fout.write("Case #%d: " % (casenr+1) + str(aa) + "\n")
    #sort_by_nonconflict(0, 0, engines, cases)
    print "engines", engines,"cases",cases

print "Time taken: ", time()-t0
    
    
    
    
    
    