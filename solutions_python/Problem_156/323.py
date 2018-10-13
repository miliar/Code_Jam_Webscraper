
# coding: utf-8

# In[1]:

get_ipython().magic(u'pylab inline')


# In[46]:

TEST = False

NAME = "2015/B-small-attempt1" # "B-large" # "B-small-attempt0" # "test" # 
INPUT_NAME = NAME + ".in"
OUTPUT_NAME = NAME + ".out"

def moves_to_threshold(item,threshold):
    if(item <= threshold):
        return 0
    return item/threshold + (-1 if item%threshold==0 else 0)

def pancakes(dish_list):
    min_moves = max(dish_list)
    if min_moves <= 3:
        return min_moves
    #min_threshold = 2
    for threshold in range(2,min_moves):
        moves = threshold
        for item in dish_list:
            moves += moves_to_threshold(item,threshold)
        if moves < min_moves:
            min_moves = moves
            #min_threshold = threshold
    #print min_threshold
    return min_moves

def check_result(dish_list):
    #return str(dish_list)
    return str(pancakes(dish_list))

output_file = open("./"+OUTPUT_NAME, 'w')
with open("./"+INPUT_NAME) as f:
    numTests = int(f.readline())
    for test in range(numTests):
        #useless line
        f.readline()
        dish_list = [int(x) for x in f.readline().split(" ")]
        if(TEST):
            print "Case #"+str(test+1)+": "+check_result(dish_list)
            print "input: "+str(dish_list)+"\n"
        else:
            output_file.write("Case #"+str(test+1)+": "+check_result(dish_list)+"\n")
output_file.close()

print "### DONE"

