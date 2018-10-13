import sys  

#f = open("inputfile", "r")
#f = open("A-small-attempt0.in", "r")
f = open("A-large.in", "r")
t = int(f.readline().strip())

#sys.stdout = open('A-small-out.txt', 'w')
sys.stdout = open('A-large-out.txt', 'w')

for case_num in range(1,t+1):
    input_line = f.readline().strip().split(" ")
    flip_size = int(input_line[1])
    str_stack = input_line[0]
    total_stack = len(str_stack)
    flip_count = 0
    
    skip_print = False
    #print (flip_size)
    #print (str_stack)
    for i in range(0,total_stack):
        if str_stack[i] == '-':
            if i + flip_size > total_stack:
                #cannot flip the pancakes for this instance
                print ("Case #{}: {}".format(case_num, "IMPOSSIBLE"))
                skip_print = True
                break
            #flip the next K pancakes
            temp_to_add = ""
            for j in range(i,i+flip_size):
                if str_stack[j] == '-':
                    temp_to_add += "+"
                else:
                    temp_to_add += "-"
            flip_count += 1
            str_stack = str_stack[:i] + temp_to_add + str_stack[i+flip_size:]
            #print (str_stack)
    
    if (skip_print == False):
        print ("Case #{}: {}".format(case_num, flip_count))

        