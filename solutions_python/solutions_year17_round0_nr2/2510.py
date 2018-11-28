import sys  

#f = open("inputfile", "r")
f = open("B-small-attempt5.in", "r")
#f = open("B-large.in", "r")
t = int(f.readline().strip())

sys.stdout = open('B-small-out.txt', 'w')
#sys.stdout = open('B-large-out.txt', 'w')

for case_num in range(1,t+1):
    str_input_num = f.readline().strip()
    len_input = len(str_input_num)

    #print ("input: ", str_input_num)

    #check for edge case when len_input = 1
    if len_input == 1:
        print ("Case #{}: {}".format(case_num, str_input_num))
        continue

    #create return_str
    return_str = ""
    do_break=False

    #find where the series stops incrementing
    for i in range(0, len_input):
        #if i is at the end, just append it
        if i == len_input - 1:
            return_str += str(str_input_num[i])
            continue
        if int(str_input_num[i]) > int(str_input_num[i+1]):
            #minus 1 to all the return_str for this digit and all equivalent digit before it
            old_return = return_str
            return_str = return_str.replace(str_input_num[i], str(int(str_input_num[i])-1))
            if (old_return != return_str):
                return_str += "9"
            else:
                return_str += str(int(str_input_num[i])-1)
            for k in range(i+1,len_input):
                return_str += "9"
            #remove leading 0s
            return_str = return_str.lstrip("0")
            print ("Case #{}: {}".format(case_num, return_str))    
            do_break = True  
            break
        else:
            return_str += str(str_input_num[i])
    if do_break == False:
        print ("Case #{}: {}".format(case_num, return_str)) 