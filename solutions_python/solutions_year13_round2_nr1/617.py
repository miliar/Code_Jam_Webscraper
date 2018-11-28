'''
Created on May 4, 2013

@author: nils
'''

def solve(armin, motes):
    motes.sort()
    return _solve(armin, motes)

def _solve(armin, motes):
    
    if armin == 1:
        return len(motes)
    
    motes.sort()
    armin, motes = consumeMotes(armin, motes)
    
    if not motes:
        return 0
    
    motesAdd = motesToAdd(armin, motes)
    
    if len(motesAdd) >= len(motes):
        return len(motes)
    
    return len(motesAdd) + _solve(armin, motesAdd + motes)
 
            

def motesRemove(armin, motes):
    return (1, armin, motes[1:])

def motesToAdd(armin, motes):
    
    motesToAdd = []
    mote = motes[0]
    while not armin > mote:
        newMote = armin - 1
        armin += newMote
        motesToAdd.append(newMote)
         
    return motesToAdd
    
def consumeMotes(armin, motes): 
    newMotes = []
    for mote in motes:
        if mote < armin:
            armin = armin + mote
        else:
            newMotes.append(mote)
        
    return (armin, newMotes)
        