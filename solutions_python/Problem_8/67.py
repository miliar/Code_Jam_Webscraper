## NUMBER SETS ##

## Thomas Pollom ##

import math

# Functions

def should_merge(list1, list2):
    for i in list1:
        for j in list2:
            if i == j:
                return True

def combine(list1, list2):
    list3 = list1
    for i in list2:
        if i not in list1:
            list3.append(i)
    return list3



def prime_test(n,p):
    """
    returns true if n has a prime factor p or greater
    """
    for i in range(2, p):
        thing = 1
        while thing == 1:
            if n % i == 0:
                n = n/i
            else:
                thing = 0
    if n == 1:
        return False
    return True

def generateLists(a, b, p):
    """
    generates a raw list of lists
    """
    list_of_listings = []
    chk_nums = []
    for i in range(2, b-a+1):
        if prime_test(i,p):
            chk_nums.append(i)
    for i in chk_nums:
        listing = []
        for j in range(a, b+1):
            if j % i == 0:
                listing.append(j)
        list_of_listings.append(listing)
    final_list = []
    for listing in list_of_listings:
        if len(listing) > 1:
            final_list.append(listing)
    return final_list

def merge_sets(list_of_listings):
    for i in range(len(list_of_listings)):
        for j in range(len(list_of_listings)):
            if i < j:
                if should_merge(list_of_listings[i], list_of_listings[j]):
                    new_list = combine(list_of_listings[i], list_of_listings[j])
                    list_of_listings.remove(list_of_listings[j])
                    list_of_listings.remove(list_of_listings[i])
                    list_of_listings.append(new_list)
                    return merge_sets(list_of_listings)
    return list_of_listings
    

def get_num_sets(a, b, p):
    big_list = merge_sets(generateLists(a, b, p))
    num_minus = 0
    for listing in big_list:
        num_minus += len(listing)
    num = b - a - num_minus + len(big_list) + 1
    return num
            
        
        

# Transform file to list.

input_file = open('/Users/scotty/Desktop/input_file11.txt', 'r')
raw_lines = input_file.readlines()
input_file.close()
lines = []
for line in raw_lines:
    line = line.rstrip('\n')
    lines.append(line)

output_file = open('/Users/scotty/Desktop/output_file11.txt', 'w')

# Solve problem.

num_cases = int(lines[0])
current_case = 1
while current_case <= num_cases:
    inputs = lines[current_case].split()
    number = get_num_sets(int(inputs[0]), int(inputs[1]), int(inputs[2]))
    output = 'Case #%s: %s' %(current_case, number)
    output_file.write(output)
    output_file.write('\n')
    print current_case
    current_case += 1

output_file.close()

print 'done'

    




