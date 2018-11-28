#!/usr/bin/env python

# Problem A. Osmos

# notes
########
# I think I should sort the motes because this will make it easier
# there is no reason to not eat the other motes in ascending order

# when adding a mote why not always add a mote as big as possible

# if you can't eat the last mote just delete it

# special case for A=1, the game is not playable

# thinking about using a recursive idea check if solvable, if not add to the motes and make the recursive call

# problem if there is a huge step in the middle and it would be quicker to
# just remove the last however many motes - how to detect and handle this?
    # check if adding to the game is better than remove from the end, aka
    # how many times do I need to grow before I can eat it? is it better to 
    # just remove
        # this actually handles the special case of the last node too


def readgame(f):
    line = f.readline()
    words = line.split()
    A = int(words[0])
    N = int(words[1])        
    
    line = f.readline()
    words = line.split()
    motes = []
    for i in range(0,N):
        motes.append(int(words[i]))
    
    return A, motes
    
def solvegame(A,motes,ops):
    
    # sort
    motes.sort()
    
    if A == 1:
        return len(motes)
    
    # play game
    iA = A
    for i in range(0, len(motes)):
        
        # keep noming
        if motes[i] < iA:
            iA += motes[i]
        
        # oh oh we're stuck add to the game
        else:
            
            # is it the last mote?
            if i+1 == len(motes):
                motes.pop()
                ops += 1
                return solvegame(A,motes,ops)    
            
            # add as big as possible mote (aka iA-1)
            else:
                # simple always add biggest but doesn't check if its better
                # to remove them all
                #motes.append(iA-1)
                #ops += 1
                #return solvegame(A,motes,ops)   
                
                iiA = iA
                count = 0
                while iiA < motes[i]:
                    iiA += iiA-1
                    count += 1
                    
                motesLeft = len(motes) - (i+1)
                # better to remove them all
                if count > motesLeft:
                    for j in range(0,motesLeft):
                        motes.pop()
                        ops += 1
                        return solvegame(A,motes,ops)
                # better to add
                else:
                    motes.append(iA-1)
                    ops += 1
                    return solvegame(A,motes,ops)
    
    return ops
    
def main():
    
    #f = open('input.txt', 'r')
    f = open('A-small-attempt0.in', 'r')
    #f = open('A-large.in', 'r')
    T = int(f.readline())
    
    out = open('output.txt', 'w')
    
    for i in range(T):
        A, motes = readgame(f)
        ops = solvegame(A,motes,0)
        out.write('Case #'+str(i+1)+': '+str(ops) +'\n')
    
if __name__ == '__main__': 
    main()
