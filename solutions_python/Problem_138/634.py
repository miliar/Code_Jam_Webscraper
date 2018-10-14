import sys
sys.setrecursionlimit(10000)

def playDWar(alice, bob, b):
    if b==0:
        return 0
    if alice[0]>bob[0]:
        return 1+playDWar(alice[1:],bob[1:],b-1)
    return playDWar(alice[1:],bob[:b],b-1)

def playWar(alice, bob):
    liveBob = bob
    score = 0
    for w in alice:
        liveBob = [w2 for w2 in liveBob if w2>w]
        score = score+1 if liveBob == [] else score
        liveBob = liveBob[1:]
    return score

for t in range(1,input()+1):
    b = input()
    alice, bob = map(float, raw_input().split()) , map(float, raw_input().split())
    alice, bob = sorted(alice), sorted(bob)
    war = playWar(alice, bob)
    dwar = playDWar(alice, bob, b)
    print 'Case #%d: %d %d'%(t, dwar, war)
    
