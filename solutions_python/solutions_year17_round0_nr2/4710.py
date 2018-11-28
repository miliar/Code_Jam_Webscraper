def checkNonDecreasing(end_integer):
    number_string = str(end_integer)
    
    nondecreasing = True
    for i in range(len(number_string)-1):
        if int(number_string[i]) > int(number_string[i+1]):
            nondecreasing = False
            break
    
    return nondecreasing
            


if __name__ == "__main__":
    
    f = open('B-small-attempt0.in.txt', 'r')
    input = f.read()
    
    #input = "4\n132\n1000\n7\n111111111111111110"
    
    input_info = input.split("\n")
    
    test_cases = input_info[0]

    
    for i in xrange(1, len(input_info)-1):
        
        
        end_integer = int(input_info[i])
        nondecreasing = False
        
        while not nondecreasing:
            
            if checkNonDecreasing(end_integer):
                decreasing = True
                break
    
            
            end_integer -= 1
    
        print "Case #" + str(i) + ": " + str(end_integer)