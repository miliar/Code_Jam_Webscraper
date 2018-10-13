from sys import argv

def min_invites(spectators):
    standed = 0
    invites = 0
    for shy, numshy in enumerate(list(spectators)):
        if (standed < shy):
            newpeople = shy-standed
            invites += newpeople
            standed += newpeople
        standed += int(numshy)
    return invites
    
with open(argv[1], 'r') as f:
    result = [min_invites(spec.split(' ')[1].strip()) for spec in list(f)[1:]]    
    for i,r in enumerate(result):
        print("Case #%d: %d"%(i+1, r));
        
