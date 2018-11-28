# python tidy.py < input_small.txt > out.txt

def print_func( par ):
#    print "Hello : ", par
    return

def checkEqual(iterator):
    return len(set(iterator)) <= 1

def decr_check(ls):
    for i in xrange(len(ls)-1,0,-1):
        if ls[i] < ls[i-1]:
            return False
    return True

def check_tidy( num ):
    
    isTidy = num
    #        check if the digits are ascending
    # check if the number has only one digit - incase of 7
    # check if all the numbers are the same - incase of 555
    # check if the reverse of the numbers is greater than n-1 th element
    
#    print str(num)
    num_str = str(num)
    
    len_num_str = len(num_str)
    

    
    if len_num_str == 1:
        return isTidy
    else:
        digit_arr = list()
        for i in xrange(len_num_str):
            digit_arr.append(num_str[i]);
        
        identi_value = checkEqual(digit_arr)
        
        if identi_value == True:
            return num
        
        else:
             
            if decr_check(digit_arr)==True:
                return num
            # check for decremented str value
    
#    return isTidy
    return 0

t = int(raw_input())

n_arr =list()
op_arr =list()

for i in xrange(1, t + 1):
    n = int(raw_input())
    n_arr.append(n)
    
    
for i in xrange(0, len(n_arr)):
#    for j in xrange(n_arr[i],n_arr[i]-4,-1):
    for j in xrange(n_arr[i],0,-1):
        
        sol = check_tidy(j)
        if sol!=0:
            op_arr.append(sol)
            break
#        print "Case #{}: {}".format(i, sol)

        
    
#  111111111111111110  
#print op_arr

for i in xrange(0, len(op_arr)):
    print "Case #{}: {}".format(i+1, op_arr[i])


    
    