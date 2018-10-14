import sys

# How many cases?
def main():
    T = int(sys.stdin.readline())
    for case in range(1,T+1):
        loop(case)
        
# Play normal war
def playWar(length,pl1,pl2):
    p1 = pl1[:]
    p2 = pl2[:]
    point = 0 # Point for p1
    
    for rnd in range(0,length):
        b1 = b2 = 0
            
        # P1 chooses lightest block
        b1 = p1[0]
    
        # P2 chooses lightest block that is still heavier than b1
        # If none available, choose lightest block
        for sb in p2:
            if sb > b1 and not b2:
                b2 = sb
        if not b2:
            b2 = p2[0]
        
        # Compare them
        if b1 > b2:
            point = point + 1
        
        # Destroy both blocks
        p1.remove(b1)
        p2.remove(b2)
    
    return point

"""
Simplified tactics of player 1 in deceitful war:
 - If player 1's lightest block is lighter than player 2's lightest block, trick player 2 to use his heaviest block
 - If player 1's lightest block is heavier than player 2's lightest block, trick player 2 to use his lightest block

With this, maximum win amount is reached
"""
def playDeceitfulWar(length,pl1,pl2):
    p1 = pl1[:]
    p2 = pl2[:]
    point = 0 # Point for P1
    
    for rnd in range(0,length):
        b1 = b2 = 0
            
        # P1 chooses lightest block
        b1 = p1[0]
                
        # Since P2 is tricked, if his lightest block is heavier than P1's lightest block, use P2's heaviest block
        if p2[0] > b1:
            b2 = p2[-1]
        # Otherwise, use his lightest block ( since he is tricked! )
        else:
            b2 = p2[0]
        
        # Compare the them
        if b1 > b2:
            point = point + 1
            
        # Destroy both blocks
        p1.remove(b1)
        p2.remove(b2)
        
    return point        

        
def loop(case):
    blocknum = int(sys.stdin.readline())
    naomi    = sys.stdin.readline().split(' ')
    naomi    = [float(x) for x in naomi]
    ken      = sys.stdin.readline().split(' ')
    ken      = [float(x) for x in ken]
    naomi.sort()
    ken.sort()

    deceitfulWar = playDeceitfulWar(blocknum,naomi,ken)
    war = playWar(blocknum,naomi,ken)
    

    sys.stdout.write("Case #{}: {} {}\n".format(case, deceitfulWar, war))
    

if __name__ == '__main__':
    main()