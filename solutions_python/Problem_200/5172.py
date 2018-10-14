def check_tidy(number):
    c_no = number
    str_number = str(number)
    digit_count = len(str_number)
    #print "number of digits ",digit_count
    last_digit = c_no%10;
    digit =0;
    step = 0
    while (c_no!=0):
        digit = c_no%10
        #print "Last digit ",last_digit
        #print "Digit      ",digit
        #print "================"
        if(last_digit>=digit):
            last_digit = digit
            step=step+1
            #print "step = ",step
        else:
            return False
        c_no = c_no/10
    if(digit_count==step):
        return True

def solve(n):
    copy_n =n
    while(copy_n !=0 ):
        #print " n= ",copy_n
        if(check_tidy(copy_n)):
            return copy_n
        copy_n = copy_n - 1
    return n

t=int(raw_input())
for x in xrange(1,t+1):
    n=int(raw_input())
    print "Case #{}: {}".format(x,solve(n))
