from sys import stdin as input
import itertools
 

for i in range(int(input.readline())):
    data = input.readline().split()
    n = data[0] #number of players
    s = int(data[1]) #number of surprising
    p = int(data[2]) #best result, response must contain >= p
    total = (data[3:]) #total scores of players 
    
    total_triplets = 0
    num_of_surprising = 0
    num_of_best_results = 0
            
    def is_impossible(triplets):
        for i,j in ([0,1],[1,2],[0,2]):
            if abs (triplets[i] - triplets[j]) >2: return True
            
        return False
    
    def is_surprissing(triplets):
        for i,j in ([0,1],[1,2],[0,2]):
            if abs (triplets[i] - triplets[j]) ==2: return True
        return False
    
    def best_result_ok(triplets):
        for i in triplets:
            if i>=p: return True
    
    for j in total:
        list_triplets = [triplets for triplets in itertools.combinations_with_replacement(range(11), 3) if sum(triplets) == int(j) and not is_impossible(triplets) and best_result_ok(triplets) ] 
        total_triplets = total_triplets + len(list_triplets)
         
        for k in list_triplets:
            if not is_surprissing(k):
                num_of_best_results += 1
            else:
                if num_of_surprising < s and len(list_triplets)==1     : 
                    num_of_best_results +=1
                    num_of_surprising +=1
    num_of_surprising = 0                    
    
    print "Case #%d: %d" % ((i+1), num_of_best_results)