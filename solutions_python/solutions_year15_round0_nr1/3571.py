import math

## Function to put numbers into dictionary -- Update for large
def num_into_dic(num, string):
    dic = {}
    for i in range(num + 1):
        dic[i] = int(string[i])
    return dic
    
## Function to return where stop
def string_stop_point(num_add_ppl, num_dict, max_len):
    i = 0
    number_standing = num_add_ppl
    while number_standing >= i and i < max_len + 1:
        number_standing += num_dict[i]
        i += 1        
    return max(0, i -1)

## ---------------------------------------------


## Open Files (Input and output)
in_file = open("problem_1_testing.txt", "r")
out_file = open("gcj_small_1.txt", "w")

## Read in number of cases
num_cases = int(in_file.readline())

## Start outer loop (Cases)
for i in range(num_cases):
    raw_string = in_file.readline().split()
    ## Take in the maximum shyness lvl
    max_shy = int(raw_string[0])
    ## Function to put numbers into dictionary
    num_dic = num_into_dic(max_shy, raw_string[1])
    
    ## Create additional ppl var = 0
    num_add_ppl = 0
    string_stop = 0
    string_stop =  string_stop_point(num_add_ppl, num_dic, max_shy)
    
    ## While return is not == max shy
    while string_stop <> max_shy:        
        ## Call Function to find where string stops
        num_add_ppl += 1
        string_stop =  string_stop_point(num_add_ppl, num_dic, max_shy)
        
    ## Write solution
    out_file.write("Case #" + str(i + 1) + ": " + str(num_add_ppl) + "\n")

## Close files
in_file.close()
out_file.close()


