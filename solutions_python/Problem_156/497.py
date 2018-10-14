
import sys
n = int(sys.stdin.readline())

table= {}

def solver(Ps):
    
    
    if all([p<=2 for p in Ps]):
        return max(Ps)
    else:
        
        Ps_sorted= sorted(Ps)
        ps_key= ",".join(map(str,Ps_sorted))
        maxP = Ps_sorted.pop()
        
        if len([p for p in Ps if p ==maxP]) >= (maxP -1):
            return maxP
        
        # Wrong!!!! half split does not promise optimal solution
#         if maxP %2 ==0:
#             Ps_actioned = Ps_sorted + [ maxP / 2,maxP/2]
#         else:
#             Ps_actioned = Ps_sorted + [ maxP / 2,maxP/2 +1]
      
        
        if ps_key in table.keys():
            return table[ps_key]
        else:
            Ps_actioned_candidates = []
            for i in range(1, maxP/2 +1):
                Ps_actioned_candidates.append( (Ps_sorted + [i , maxP-i] ))
            
            actioned_min = min(map(solver,Ps_actioned_candidates)) +1
            
            if maxP <= actioned_min:
                #elif maxP <= solver(Ps_actioned) +1:
                table[ps_key] = maxP
                return maxP
            else:
                return actioned_min
        


for case_i in range(n):
    D = int(sys.stdin.readline())
    Pis = map(int,sys.stdin.readline().split())
    solution = 1
    #print Pis
    solution = solver(Pis)
    
    #print "Case #{0}: {1}, {2}".format(case_i+1, solution,Pis)
    print "Case #{0}: {1}".format(case_i+1, solution)