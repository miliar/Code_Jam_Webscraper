import math
T = int(raw_input().strip())
for i in range(T):
#    print "case #: ", i+1

    temp = map(int, raw_input().strip().split(" "))
    N = temp[0] # number of ingredients
    P = temp[1] # number of packages of each ingredient
    recipe = map(int, raw_input().strip().split(" "))
    
    
    portions = []
    ingredients = [] # I can delete this later
    for j in range(N): # for each ingredient
        tempI = sorted(map(int, raw_input().strip().split(" ")), reverse = True)
        tempP = []
        for k in range(P): # for each package of that ingredient
            tempP.append(float(tempI[k])/recipe[j])
        portions.append(tempP)
        ingredients.append(tempI) # I can delete this later

#    print "N = ", N
#    print "P = ", P
#    print "recipe = ", recipe
#    print "ingredients = ", ingredients
#    print "portions = ", portions

    answer = 0
    
    done = False
    while done == False:
        portions.sort(key=lambda x: x[0], reverse = True)
#        print "portions.sort = ", portions
        numPortions = math.ceil(portions[0][0]/1.1)
#        print "numPortions = ", numPortions
        #break
        if portions[-1][0] >= numPortions * 0.9 and portions[0][0] >= numPortions * 0.9:
#            print "in first if"
            answer += 1
            for k in range(len(portions)):
#                print "k = ", k
#                print "len(portions[k]) = ", len(portions[k])
                if len(portions[k]) > 1:
                    portions[k] = portions[k][1:]
                else: 
                    done = True
                    break
        else:
#            print "in else"
            if len(portions[0]) > 1:
                portions[0] = portions[0][1:]
            else:
                done == True
                break
#    print "answer = ", answer
#    print " "
        
    print "case #" + str(i+1) + ": " + str(answer)
