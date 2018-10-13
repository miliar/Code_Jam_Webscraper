# breaks for sample case 4

import sys
sys.setrecursionlimit(100000)

def is_tidy(number):
    number_array = map(int,str(number))

    for i in xrange(0,len(number_array)-1): 
        if number_array[i] > number_array[i+1]: 
            number_array = set_next_digits_to_zero(number_array,i+1)
            return False, number_array
    return True,number_array


def set_next_digits_to_zero(array,index):
    array[index:len(array)-1] = [0]*(len(array)-1-index)

    number = map(str,array)
    number = ''.join(number)
    number = int(number)
    return number

def tidy_loop(num):
    tf,newnum = is_tidy(num)
    if tf:
        return num
    else:
        return tidy_loop(newnum-1)

    # for n in xrange(num,0,-1):
    #     if is_tidy(n)[0]:
    #         return n
    #     else:
    #         continue
        

t = int(raw_input())
for i in xrange(1,t+1):
    the_number = int(raw_input())

    print "Case #{}: {}".format(i,tidy_loop(the_number))
