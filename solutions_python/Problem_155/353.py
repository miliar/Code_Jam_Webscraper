
# coding: utf-8

# In[1]:

get_ipython().magic(u'pylab inline')


# In[24]:

TEST = False

NAME = "2015/A-small-attempt0" # "A-large-practice" # "A-small-practice" # 
INPUT_NAME = NAME + ".in"
OUTPUT_NAME = NAME + ".out"

def standing_ovation(line):
    to_add = 0
    #print "+"+line+"+", len(line)
    sum = int(line[0])
    for index in range(1,len(line)):
        #print line[index]
        num = int(line[index])
        if num != 0:
           #print sum, "<", index
            if sum < index:
                to_add += index-sum
                #print "add", to_add
                sum = index + num
            else:
                sum += num
    return to_add

def check_result(line):
    return str(standing_ovation(line))

output_file = open("./"+OUTPUT_NAME, 'w')
with open("./"+INPUT_NAME) as f:
    numTests = int(f.readline())
    for test in range(numTests):
        [S_max, line] = [x for x in f.readline().split(" ")]
        line = (line.split("\n"))[0]
        if(TEST):
            print "Case #"+str(test+1)+": "+check_result(line)+"\n"
        else:
            output_file.write("Case #"+str(test+1)+": "+check_result(line)+"\n")
output_file.close()

print "### DONE"


# In[ ]:



