from itertools import product, permutations
import copy
import sys

def solve(recipe,ingredients):
    P = len(ingredients[0])
    
    if P == 0:
        return 0
    
    N = len(recipe)
    
    min_packets = max(1, int(min(ingredients[0])  * 0.9 / recipe[0] / 1.1) - 2)
    max_packets = int(max(ingredients[0])  * 1.1 / recipe[0] / 0.9) + 2
    
    #print ingredients, min_packets, max_packets    
    
    
    best = 0

    
    
    for i in range(min_packets,max_packets):
        #try to make packets of i serves
        packet = []
        options = []
        for j in range(N):
            ingoptions = []
            for packet in ingredients[j]:
                if (0.9 <= 1.0 * packet / (recipe[j]*i) <= 1.1):
                    ingoptions.append(packet)
            options.append(ingoptions)
            
        #print "options", i, options
            
        for option in product(*options):
            #print P, i, option
            newingred = copy.deepcopy(ingredients)
        
            for i in range(len(option)):
                p = option[i]
                for j in range(len(newingred[i])):
                    if newingred[i][j] == p:
                        newingred[i] = newingred[i][:j] + newingred[i][j+1:]
                        break
                
            soln = solve(recipe, newingred)
            if soln + 1 > best:
                best = soln + 1
                if best == P:
                    return best
                
    return best

def parse(text):
    T = int(text.next())
    for i in range(T):
        line = text.next().rstrip().split(" ")
        N = int(line[0])
        P = int(line[1])
        
        line = text.next().rstrip().split(" ")
        recipe = [int(x) for x in line]
        
        ingredients = []
        for _ in range(N):
            line = text.next().rstrip().split(" ")
            packets = [int(x) for x in line]
            ingredients.append(packets)
            
        soln = solve(recipe,ingredients)
        
        print "Case #%d: %d" % (i+1, soln)
        sys.stdout.flush()
		
parse(sys.stdin)
