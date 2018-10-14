def isPalindrom(num):
    if num < 10:
        return True
    num_str = str(num)
    strlen = len(num_str)
    for i in xrange(strlen/2 + 1):
        if num_str[i] != num_str[strlen - i -1]:
            return False
            
    return True

def populate_sqr_map_list(sqr_map):
    for i in xrange(10000000):
        sqr_i = i*i
        if isPalindrom(i) and isPalindrom(sqr_i):
            sqr_map[i*i] = i


def parse_file(input_file):
    T = int(input_file.readline().replace('\n',''))
        
    output_file = file("C-large-1.out", "w")
    
    sqr_map = {}
    
    populate_sqr_map_list(sqr_map)
    keys = sqr_map.keys()
    keys.sort()
    print keys
    #print sqr_map
    for test_case_counter in xrange(T):
        v1 = input_file.readline().replace('\n','').split(' ')
        A = int(v1[0])
        B = int(v1[1])
        
        i = A
        #print A, B
        fns = 0
        for key in keys:
            if key >= A:
                if key <= B:
                    fns = fns + 1
                else:
                  break
                              
        output_file.write("Case #"+str(test_case_counter+1)+": "+ str(fns)+"\n") 

    output_file.close()
    
if __name__ == "__main__":
    input_file = file("C-large-1.in")
    parse_file(input_file)
    #print isPalindrom(121)
