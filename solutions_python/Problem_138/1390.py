import sys
import copy



def triche(poids_naomi, poids_ken):
#     print poids_naomi
#     print poids_ken
    
    score = 0
    
    
    for i in range(len(poids_naomi)):
        n = poids_naomi.pop(0)
        
#         print "n:", n
        
        
        
        if n > poids_ken[0]:
#             print "kz", poids_ken[0]
            poids_ken.pop(0)
            score+=1
        else:
            poids_ken.pop()
            
        
    return score


def optim(poids_naomi, poids_ken):
    score = 0
    
    for w in range(len(poids_ken)):
    
        n = poids_naomi.pop() # plus gd des poids de naomi
        
        if n > poids_ken[-1]:
            poids_ken.pop(0)
            score+=1
        else:
            for i,p in enumerate(poids_ken):
                if p>n:
                    del poids_ken[i]
                    break
    return score
    
    







f=open(sys.argv[1])

t = int(f.readline())

for i in range(t):
    f.readline()
    poids_naomi = [ float(k) for k in f.readline().split() ]
    poids_ken = [ float(k) for k in f.readline().split() ]
    
    score = 0
    
    poids_naomi.sort()
    poids_ken.sort()
    
    tr = triche(copy.copy(poids_naomi), copy.copy(poids_ken))
    op = optim(copy.copy(poids_naomi), copy.copy(poids_ken))
    
    
    print "Case #%i: %i %i"%(i+1, tr, op )
    
    