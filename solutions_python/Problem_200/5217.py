input_file = open("B-small-attempt2.in", "r")
count = 1
for i in input_file.readlines()[1:]:
    
    num = int(i)
    num_list1 = []
    num_list2 = []
    while num>0:
        num_list1 = [int(d) for d in str(num)]
        num_list2 = [int(d) for d in str(num)]
        num_list2.sort()
        if num_list1 == num_list2:
            num_out = int(''.join(map(str,num_list1)))
            print "Case #"+str(count)+":",num_out
            break
        num = num-1
    count = count+1
            
        

    
