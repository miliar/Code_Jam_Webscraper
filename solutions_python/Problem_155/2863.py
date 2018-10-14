import sys
 
def main():
    n_cases = int(sys.stdin.readline())


    ##could improve this to a more efficient search by sorting the list... maybe one day...
    for test_case in range(1, n_cases + 1):
    
        #max_shy = int(sys.stdin.read())
        #values = int(sys.stdin.read())
        #print max_shy, " ", values
        case_in = sys.stdin.readline()
        #print case_in
        
        
        case_in = case_in.split("\n")[0]
        aux = case_in.split(" ")
        #print aux
        max_shy = int(aux[0])
        values = aux[1]
        
        persons = []
        for person in range(0, max_shy+1):
            persons.append(int(values[person]))
            
        #print persons
        guests = 0
        persons_count = 0
        for p in range(0, max_shy+1):
            if persons[p] > 0:
                if p > persons_count:
                    need_to_add = p - persons_count
                    guests += need_to_add
                    persons_count += need_to_add
            persons_count += persons[p]
        print "Case #" + str(test_case) + ": " + str(guests) 
        
main()