#! /usr/bin/env python

input_file = "input.txt"

def is_tidy(n):
    #Check if all the digits of a number are sorted in ascending order
    while(n > 1):
        cur_dig = n % 10
        n = n / 10
        next_dig = n % 10
        if cur_dig < next_dig:
            return False
    return True

def print_result(case_no, result):
    print "Case #" + str(case_no) + ": " + str(result)

def find_ooo_index(n_str):
    for i in range(len(n_str) - 1):
        if n_str[i] > n_str[i+1]:
            #I is the first out of order number, but first check if i is repeated at all.
            if (i > 0 and n_str[i-1] == n_str[i]): 
                j = i-1
                while (j > 0) and n_str[j] == n_str[i]:
                    j -= 1 
                return j
            else:
                return i
    return -1

def find_tidy(n_str):
    #This one takes in n as a string
    if len(n_str) == 1:
        return int(n_str)

    index = find_ooo_index(n_str)
    if index == -1:
        return int(n_str)

    tidy_str = n_str[:index] + str(int(n_str[index]) - 1) + ('9' * (len(n_str) - index - 1))
    return int(tidy_str)
                

def main():
    with open(input_file, 'r') as f:
        T = int(f.readline()) #T contains the no. of test cases
        for i in range(T):
            n = f.readline().strip()
            print_result(i + 1, find_tidy(n))


main()
