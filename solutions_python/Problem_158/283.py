
# coding: utf-8

# In[1]:

#%pylab inline


# In[7]:

TEST = False

NAME = "2015/D-small-attempt0" # "D-large" # "D-small-attempt0" # "test" # 
INPUT_NAME = NAME + ".in"
OUTPUT_NAME = NAME + ".out"

def gabriel_win(X,R,C):
    dim_max = max(R,C)
    dim_min = min(R,C)
    return X <= 6 and ((R*C)%X == 0) and (dim_max >= X and dim_min >= X-1)

def check_result(X,R,C):
    res = gabriel_win(X,R,C)
    if res:
        return "GABRIEL"
    return "RICHARD"

output_file = open("./"+OUTPUT_NAME, 'w')
with open("./"+INPUT_NAME) as f:
    numTests = int(f.readline())
    for test in range(numTests):
        [X,R,C] = [int(x) for x in f.readline().split(" ")]
        if(TEST):
            print "Case #"+str(test+1)+": "+check_result(X,R,C)
            #print "input: "+str(str_list)+"\n"
        else:
            output_file.write("Case #"+str(test+1)+": "+check_result(X,R,C)+"\n")
output_file.close()

print "### DONE"


# In[ ]:



