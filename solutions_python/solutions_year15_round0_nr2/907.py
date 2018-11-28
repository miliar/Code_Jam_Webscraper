import itertools

num_cases = input()
cases = []

for x in range(num_cases):
    D = input()
    D_list = raw_input()
    D_list = [int(i) for i in D_list.split()] # Split str line into int array
    cases.append((D, D_list))

counter = 0
for case in cases:
    min_result = 100
    results = []
    counter += 1
    #print "Case", counter
    D = case[0]
    D_list = case[1]
    #print "D_list", D_list

    max_mins = max(D_list) # Number of mins required with no intervention
    #print "max mins", max_mins

    # Get special minute perms
    special_mins = ["".join(i) for i in itertools.product("01", repeat=max_mins)]


    # Special case hack
    if len(D_list) == 1 and D_list[0] == 1:
        min_result = 1

    # loop through trying special min on each minute
    for perm in special_mins:
        for give in range(1, max(D_list)):
            tmp_list = D_list[:]
            #print "tmp_list at start", tmp_list
            #print "D list at start", D_list
            #print "Perm", perm
            for minute in range(len(perm)):
                #print "Minute", minute
                if perm[minute] == '1':
                    # special minute
                    #print "Special Minute!"
                    #print "Before", tmp_list
                    if give >= max(tmp_list):
                        #give2 = max(tmp_list)
                        break
                    else:
                        give2 = give
                    tmp_list[tmp_list.index(max(tmp_list))] -= give # decrement max element
                    tmp_list.append(give) # Give pancake to person with empty plate
                    #print "After", tmp_list
                    #print ""
                   
                else:
                    # normal minute
                    #print "Normal minute"
                    #print "Before", tmp_list
                    tmp_list = [i-1 for i in tmp_list] # decrement all
                    #print "After", tmp_list
                    #print ""

                # Check if finished
                check = True
                for plate in tmp_list:
                    if plate > 0:
                        check = False
                if check is True:
                    if (minute+1) < min_result:
                        min_result = minute+1
                    results.append((perm, minute+1))
                    break;
            
    print "Case #" + str(counter) + ":", min_result
