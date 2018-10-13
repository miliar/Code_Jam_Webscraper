import sys

fname = sys.argv[1]

handler = open(fname, "r")
lines = [line.strip() for line in handler]

T = int(lines.pop(0))

def war(naomi, ken, deceitful):
    a = list(naomi)
    b = list(ken)

    if deceitful: a.sort()
    b.sort()
    N = len(a)
    
    naomi_score = ken_score = 0
    
    for _ in range(N):
        if deceitful:
            lighter_blocks = [x for x in a if x < b[0]]
            
            if len(lighter_blocks):
                # play lightest blocks (that cannot win) from a with the heaviest blocks from b
                chosen_a = a.pop(0)
                chosen_b = b.pop()
            else:
                if b[-1] > a[-1]:
                    chosen_a = a.pop(0)
                    chosen_b = b.pop()
                else:
                    chosen_a = a.pop()
                    chosen_b = b.pop()
        else:
            chosen_a = a.pop(0)
        
            heavier_blocks = [x for x in b if x > chosen_a]
            
            if len(heavier_blocks):
                chosen_b = heavier_blocks.pop(0)
                b.remove(chosen_b)
            else:
                chosen_b = b.pop(0)
            
        if chosen_a > chosen_b:
            naomi_score += 1
        else:
            ken_score += 1
    
    return naomi_score

for case in range(T):
    blocks_count = int(lines.pop(0))
    a = map(float, lines.pop(0).split(' '))
    b = map(float, lines.pop(0).split(' '))
    
    score1 = war(a, b, deceitful=True)
    score2 = war(a, b, deceitful=False)
    
    print "Case #%d: %d %d" % (case+1, score1, score2)
	
handler.close()