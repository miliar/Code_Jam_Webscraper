## Get the nearest neighbor distance for each empty stall in the list of stalls. 
def getDistances(stalls):
    distances_left = []
    distances_right = []
    for i in range(len(stalls)):
        if stalls[i] == 0: # stall is empty
            if i != 0:
                distances_left.append(distances_left[i - 1] + 1)
            if i >= len(distances_right): # We have not filled this out yet. 
                j = i
                while stalls[j] == 0:
                    maxDistance = 1 + (j - i)
                    j += 1
                for j in range(0, maxDistance):
                    distances_right.append(maxDistance - j - 1)
        else: # Stall is not empty. 
            distances_left.append(-1)
            distances_right.append(-1)
    return (distances_left, distances_right)
def choosePosition(distances_left, distances_right):
    #~ print "We think left dist is ", distances_left    
    #~ print "Right dist is ", distances_right
    first_consideration = []
    for i in range(len(distances_left)):
        first_consideration.append(min(distances_left[i], distances_right[i]))
    #~ print "First considerations gets us ", first_consideration
    best = max(first_consideration)
    maxes= []
    for index, score  in enumerate(first_consideration):
        if score == best:
            maxes.append(index)
    if len(maxes) == 1:
        return maxes[0]
    second_consideration = []
    for i in maxes:
        second_consideration.append(max(distances_left[i], distances_right[i]))
    #~ print "second consideration gets us ", second_consideration
    best_score = max(second_consideration)
    for i in range(0, len(second_consideration)):
        if second_consideration[i] == best_score:
            #~ print "We decide to place ourselves at index ", maxes[i]
            return maxes[i]
    print "WE ARE VERY SAD"

    
T = int(raw_input())
for case in range(T):
    n_stalls, n_people = ((raw_input()).strip()).split()
    #~ print "nr stalls ", n_stalls, " nr people", n_people
    n_stalls = int(n_stalls)
    n_people = int(n_people)
    ## Intiiate our stalls vector. 
    stalls = [1]
    for s in range(n_stalls):
        stalls.append(0)
    stalls.append(1)
    distances_left = []
    distances_right = []
    for p in range(n_people):
        #~ print "stalls is ", stalls
        distances_left, distances_right = getDistances(stalls)
        
        index = choosePosition(distances_left, distances_right)
        stalls[index] = 1
    
    LS = distances_left[index]
    RS = distances_right[index]
    print "Case #"+str(case+1)+":  "+str( max(LS, RS)) + " " + str(min(LS, RS))
