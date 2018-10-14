import numpy as np

def is_tidy_brute(number):
    
    num_list = []
    str_number = str(number)
    is_tidy = False
    for ii in range(len(str_number)):
        num_list.append(str_number[ii])

    num_sorted = np.sort(num_list)
    num_sorted_list = np.ndarray.tolist(num_sorted)

    if(num_sorted_list == num_list):
        is_tidy = True
        
    return is_tidy


def find_max_tidy(number):
    max_tidy = 0
    for ii in range(1,number+1):

        if (is_tidy_brute(ii) == True):
            max_tidy = ii
    return max_tidy

# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    n = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
    n = n[0]
    max_tidy = find_max_tidy(n)
    print "Case #{}: {}".format(i, max_tidy)
  # check out .format's specification for more formatting options
