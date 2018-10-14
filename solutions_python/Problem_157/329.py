
# coding: utf-8

# In[1]:

get_ipython().magic(u'pylab inline')


# In[3]:

TEST = True

NAME = "2015/C-small-attempt2" # "C-large" # "C-small-attempt1" # "test" # 
INPUT_NAME = NAME + ".in"
OUTPUT_NAME = NAME + ".out"

def quat_mul(sign,first,second):
    if(first == second):
        return[-sign,'']
    if(first == '' or second == '' ):
        return[sign,first+second]
    if(first == 'i'):
        if(second == 'j'):
            return[sign,'k']
        return[-sign,'j'] # second == 'k'
    if(first == 'k'):
        if(second == 'i'):
            return[sign,'j']
        return[-sign,'i'] # second == 'j'
    #first == 'j'
    if(second == 'i'):
        return[-sign,'k']
    return[sign,'i'] # second == 'k'

def quat_mul_list(str_list,index):
    if(len(str_list)-index == 0):
        return[1,'']
    mul = str_list[index]
    sign = 1
    for item in str_list[index+1:]:
        [sign,mul] = quat_mul(sign,mul,item)
    return [sign,mul]

def reduce_to(str_list,index,quat_init,quat):
    length = len(str_list)
    if(index >= length):
        return index
    #index = 1
    [sign,mul] = quat_mul(1,quat_init,str_list[index])
    index += 1
    while (index < length and (mul != quat or sign == -1)):
        [sign,mul] = quat_mul(sign,mul,str_list[index])
        index += 1
    return index

def check_k(str_list,index):
    #print "check_k:", index#,str_list
    [sign,mul] = quat_mul_list(str_list,index)
    #print mul
    return sign == 1 and mul == 'k'

def check_jk(str_list,index):
    #print "check_jk:", index#,str_list
    length = len(str_list)
    if(length - index < 2):
        return False
    if(str_list[index] == 'j'):
        if check_k(str_list,index+1):
            return True
    #index = 0
    quat = ''#str_list[index]
    #list_tmp = str_list[:]
    #while index < length:
    index = reduce_to(str_list,index,quat,'j')
        #list_tmp = list_tmp[index:]
    if check_k(str_list,index):
        return True
    #quat = 'j'
        #list_tmp = 'j'+list_tmp
        #length = len(list_tmp)
    return False

def check_ijk(str_list):
    #print "check_ijk:", 0#,str_list
    length = len(str_list)
    if(length < 3):
        return False
    if(str_list[0] == 'i'):
        if check_jk(str_list,1):
            return True
    index = 0
    quat = ''#str_list[index]
    #list_tmp = str_list[:]
    #while index < length:
    index = reduce_to(str_list,index,quat,'i')
    #list_tmp = list_tmp[index:]
    if check_jk(str_list,index):
        return True
    #quat = 'i'
        #list_tmp = 'i'+list_tmp
        #length = len(list_tmp)
    return False

def check_result(str_list):
    [sign,mul] = quat_mul_list(str_list,0)
    if(mul == '' and sign == -1):
        if(check_ijk(str_list)):
            return "YES"
    return "NO"

output_file = open("./"+OUTPUT_NAME, 'w')
with open("./"+INPUT_NAME) as f:
    numTests = int(f.readline())
    for test in range(numTests):
        [length,times] = [int(x) for x in f.readline().split(" ")]
        str_list = f.readline().split("\n")[0]
        str_list = str_list * times
        if(TEST):
            print "Case #"+str(test+1)+": "+check_result(str_list)
            #print "input: "+str(str_list)+"\n"
        else:
            output_file.write("Case #"+str(test+1)+": "+check_result(str_list)+"\n")
output_file.close()

print "### DONE"


# In[ ]:



