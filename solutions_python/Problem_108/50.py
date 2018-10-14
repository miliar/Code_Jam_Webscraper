# -*- coding: utf-8 -*-
# <nbformat>3</nbformat>

# <codecell>

def readline_ints():
    return [int(num) for num in fin.readline().strip().split()]

# <codecell>

class Vine:
    def __init__(self, root, length):
        self.root = root
        self.length = length
        self.best_swing = 0

# <codecell>

def pick_next_vine(current_root, current_reach, vines):
    next_root = None
    best_potential_reach = current_reach
    for v_root, v_length in vines:
        if v_root > current_reach:
            break
        potential_reach = v_root + min(v_root-current_root, v_length)
        if potential_reach > best_potential_reach:
            best_potential_reach = potential_reach
            next_root = v_root
    
    return next_root, best_potential_reach

# <codecell>

def is_swingable(vines, final):
    vines[-1].best_swing = vines[-1].root
    current_reach = 0
    
    while current_reach < final:
        myvine = vines.pop()
        if myvine.best_swing == 0:
            return False

        current_reach = myvine.root + myvine.best_swing
        for vine in reversed(vines):
            if vine.root > current_reach:
                break
            potential_swing = min(vine.root-myvine.root, vine.length)
            vine.best_swing = max(potential_swing, vine.best_swing)
    
    return True
            

# <codecell>

# Update this with the filename
fname = "A-large"
with open(fname+".in","r") as fin, open(fname+".out","w") as fout:

    numcases = readline_ints()[0]
    print(numcases, "cases")
    
    for caseno in range(1, numcases+1):
        # Code goes here
        N = readline_ints()[0]
        print(N)
        vines = [Vine(*readline_ints()) for _ in range(N)]
        final = readline_ints()[0]
        vines.append(Vine(final, 0))
        vines.reverse()
        
        result = "YES" if is_swingable(vines, final) else "NO"
        
        outstr = "Case #%d: %s" % (caseno, result)
        fout.write(outstr + "\n")
        print(outstr)

# <codecell>


