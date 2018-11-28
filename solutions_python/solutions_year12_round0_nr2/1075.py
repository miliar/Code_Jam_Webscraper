'''
Created on Apr 14, 2012

@author: ashishgaunkar
'''
import re
input_path = '/Users/ashishgaunkar/Desktop/ws/codejam/B-large.in'
output_path = '/Users/ashishgaunkar/Desktop/ws/codejam/B-large.op'
    

def best_in_triplet(triplet, best, suprising):
    '''
    check if best is possible
    '''
    is_best = False 
    if not triplet:
        return (is_best, suprising)
    rest_two = triplet - best
    print rest_two
    if int(rest_two/2) >= (best-1) :
        return (True , suprising)
    elif suprising > 0:
        print "rest-two %s"%rest_two
        if int(rest_two/2) >= (best-2) :
            return (True , suprising-1)
        
    return (is_best, suprising)

def num_of_valid_triplet( result_set, best, suprising ):
    '''
    @type total_results: int
    @type suprising: int
    @type best: int
    @type result_set: list
    
    This checks if the triplet is valid (has best result of greate then equal to P),
    in the sense that diff between any two vlaue is max - 1 
    or 2 if , we are still allowed to use the surprising marsheet where diff of 2 is allowed.
    Difference of more than 3 is not allowed
    '''
    best_count = 0
    
    for triplet in result_set:
        #print triplet
        is_best , suprising = best_in_triplet(triplet, best, suprising)
        #print is_best , suprising

        if is_best:
            best_count +=1
        
    return best_count
    
    
if __name__ == '__main__':

    fd_read = open(input_path)
    fd_write = open(output_path, 'w')
    #fd_write.write("Output\n")
    
    content = fd_read.readline() #ignore first line
    count = int(content)
    i = 1
    while (content != ""  and i <= count):
        content = fd_read.readline()
        numbers = re.findall(r'\w+', content)
        if not numbers:
            break
        print "Calulating for result_set :"+str(i)
        fd_write.write ("Case #"+str(i)+": ")
        suprising = int(numbers[1])
        best = int(numbers[2])
        total = int(numbers[0])
        triplet_list =[]
        j=0
        while(j<total):
            triplet_list += [int(numbers[3+j])]
            j += 1
            #fd_write.write()
        if best ==0:
            best_count = total
        else:
            best_count = num_of_valid_triplet(triplet_list, best, suprising )
        fd_write.write(str(best_count)+"\n")
        i +=1
        


