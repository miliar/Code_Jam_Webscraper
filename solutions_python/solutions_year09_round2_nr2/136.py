#############################
# Script description


import string
import time
import copy


##################
# Main function  #
##################
in_file_name = "B-large.in"
#in_file_name = "B-small-attempt1.in"
#in_file_name = "simple.in"
in_file= open(in_file_name, 'r')

out_file = open('out.txt','w')


num_of_testcases = int(in_file.readline())
for count in range (0,num_of_testcases):
    cnt = count
    print "Time %03d sec" % (time.clock())
    print "testcase : " , str(count+1), "out of" , num_of_testcases
    num_as_str = in_file.readline()[:-1]
    print num_as_str
    num_as_list =  list(num_as_str)
    for i in range (0,len(num_as_list)):
        num_as_list[i] = int(num_as_list[i])
    #print num_as_list
    done = 0
    
    #while done == 0:
    for count in range (2,len(num_as_list)+1):
        i#print num_as_list[-count]
        if num_as_list[-count] == 9:
            continue
        num_to_search = num_as_list[-count]+1
        while num_to_search < 10:
            #print "HERE"
            #print num_as_list[-count-1:]
            for num in num_as_list[-count+1:]:
                #print num_as_list[-count+1:]
                if int(num) == num_to_search:
                    #print "HERE", num 
                    switch_ind = num_as_list[-count+1:].index(num)
                    tmp = num
                    #print tmp, num_as_list[-count],num_as_list[-count+1:][switch_ind] 
                    num_as_list[-count+1+switch_ind] = num_as_list[-count]
                    #print tmp, num_as_list[-count],num_as_list[-count+1:][switch_ind]
                    num_as_list[-count] = tmp
                    done = 1
                    #print "HERE", switch_ind, count, num, tmp
                    num_as_list[-count+1:] = sorted(num_as_list[-count+1:])
                    break
            if (done == 1):
                break
            num_to_search = num_to_search+1
        if (done == 1):
            break
    #print num_as_list
    if done == 0 :
        num_as_list = sorted(num_as_list)
        for i in range (0,len(num_as_list)):
            if i == 0 and num_as_list[i]>0:
                num_as_list.insert(1,0)
                break
            if num_as_list[i]>0:
                tmp = num_as_list[i]
                num_as_list[i] = num_as_list[0]
                num_as_list[0] = tmp
                num_as_list.insert(1,0)
                break
    num_as_str=''
    for i in range (0,len(num_as_list)):
        num_as_str+=str(num_as_list[i])
    print num_as_str
    print >> out_file, 'Case #'+str(cnt+1)+':',num_as_str
    

        

###Parse in file
##num_of_letters, num_of_words, num_of_testcases = in_file.readline().split( )
###print num_of_letters, num_of_words, num_of_testcases
###Sample words
##words = []
##for count in range (0,int(num_of_words)):
##    words.append(in_file.readline())
###for word in words:
###    print list(word)[:-1]
##for count in range (0,int(num_of_testcases)):
##    print "Time %03d sec" % (time.clock())
##    print "testcase : " , count, "out of" , int(num_of_testcases) 
##    testcase = []
##    str_to_add = ''
##    inside = 0
##    for char in list(in_file.readline()):
##        if inside == 0:
##            if char != '(' and char != ')' :
##                testcase.append(char)
##            if char == '(':
##                inside = 1
##        else: #if inside == 1:
##            if char != ')':
##                str_to_add=str_to_add+char
##            if char == ')':
##                testcase.append(str_to_add)
##                inside = 0
##                str_to_add = ''
##    #print testcase
##    #Check for each word if it is inside testcase
##    total = 0
##    for word in words:
##        success = 1
##        for idx in range (0,int(num_of_letters)):
##            success = success * list(testcase[idx]).count(word[idx])
##        total = total + success
##    print >> out_file, 'Case #'+str(count+1)+':',total
    
#Close files
in_file.close()
out_file.close()


