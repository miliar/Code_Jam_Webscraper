#############################
# Script description


import string

def num_of_repeat(large_list, small_list):
    result = 0
    idx = 0
    if len(small_list) == 1:
        return large_list.count(small_list[0])
    else :
        idx = 0
        for elem in large_list:
            if elem == small_list[0]:
                result = result + num_of_repeat(large_list[idx:], small_list[1:])
            idx = idx+1
        return result
   


##################
# Main function  #
##################
#in_file_name = "A-large.in"
in_file_name = "C-small-attempt1.in"
#in_file_name = "simple.in"
in_file= open(in_file_name, 'r')

out_file = open('out.txt','w')

#Parse in file
num_of_tescases = in_file.readline()
for cnt in range (1,int(num_of_tescases)+1):
    print >> out_file,  "Case #%d: %04d" % (cnt, num_of_repeat (list(in_file.readline()), list('welcome to code jam')))
    #print >> out_file,  "Case #"+str(cnt)+':'+ ' '+str(num_of_repeat (list(in_file.readline()), list('welcome to code jam'))%10000)


    
#Close files
in_file.close()
out_file.close()


