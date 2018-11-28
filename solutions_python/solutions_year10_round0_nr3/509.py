# Theme-park Google-Code Jam 2010 (World)
# Javier Fernandez (javierfdr@gmail.com)

# Find initial cicle array and pattern
def find_pattern(groups,k):
    l = len(groups)
    index =0 #group index
    acum = 0 #acum number of persons
    g_order = [] #inner group
    g_set = set() 
    added = 0 #number of cicles in g_set

    cicle_size = 0
    cicle = []    
    while(True):
        if(acum+groups[index] > k or cicle_size==l):            
            g_set.add(tuple(cicle))
            if (len(g_set) == added): #found pattern
                rep_index = g_order.index(cicle)
                
                w_sum = []
                for kk in g_order:
                    acum = 0
                    for e in kk:                        
                        acum+= groups[e]
                    w_sum.append(acum)
                    
                               
                sl_w = w_sum[rep_index:]                                
                return [sl_w,w_sum]
                
            g_order.append(cicle)
            added+=1
            acum = 0
            cicle = []
            cicle_size = 0
            
        else:
            cicle.append(index)
            cicle_size+=1
            acum += groups[index]
            index+=1
                            
        if (index==l):
            index =0

def ride_earning(r,k,groups):
    [pattern,np] = find_pattern(groups,k)
    p_sum = sum(pattern)
    np_sum = sum(np)
    p_size = len(pattern)
    np_size = len(np)

    if (r<np_size):
        return sum(np[0:r])
    
    rest = r - np_size
    extra = rest%p_size

    result = sum(pattern[:extra])
    result+= ((p_sum*(rest/p_size)) + np_sum)

    return result


import sys

out_file = open('output.out','w+')
in_file = sys.stdin
num_cases = int(in_file.readline())

for c in range(1,num_cases+1):
    tok = map(int,in_file.readline().strip('\n').split())
    groups = map(int,in_file.readline().strip('\n').split())
       
    case = 'Case #'+str(c)+': '
    res = ride_earning(tok[0],tok[1],groups)
    out_file.write(case+str(res)+'\n')        
    
