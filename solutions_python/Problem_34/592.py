#############################
# Script description


import string


##################
# Main function  #
##################
in_file_name = "A-large.in"
#in_file_name = "A-small-attempt0.in"
#in_file_name = "simple.in"
in_file= open(in_file_name, 'r')

out_file = open('out.txt','w')


#Parse in file
num_of_letters, num_of_words, num_of_testcases = in_file.readline().split( )
#print num_of_letters, num_of_words, num_of_testcases
#Sample words
words = []
for count in range (0,int(num_of_words)):
    words.append(in_file.readline())
#for word in words:
#    print list(word)[:-1]
for count in range (0,int(num_of_testcases)):
    testcase = []
    str_to_add = ''
    inside = 0
    for char in list(in_file.readline()):
        if inside == 0:
            if char != '(' and char != ')' :
                testcase.append(char)
            if char == '(':
                inside = 1
        else: #if inside == 1:
            if char != ')':
                str_to_add=str_to_add+char
            if char == ')':
                testcase.append(str_to_add)
                inside = 0
                str_to_add = ''
    #print testcase
    #Check for each word if it is inside testcase
    total = 0
    for word in words:
        success = 1
        for idx in range (0,int(num_of_letters)):
            success = success * list(testcase[idx]).count(word[idx])
        total = total + success
    print >> out_file, 'Case #'+str(count+1)+':',total
    
#Close files
in_file.close()
out_file.close()


