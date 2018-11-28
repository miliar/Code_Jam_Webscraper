#Problem A. Standing Ovation
#Author: Saurabh Agrawal
#Date: 11th April 2015

def find_no_of_friends_to_invite(max_shyness, string_of_person_with_different_shyness_level):
    if max_shyness == 0:
        return 0

    no_of_persons = 0
    no_of_friends_to_invite = 0
    i = 1
    while i <= max_shyness:
        no_of_persons = no_of_persons + int(string_of_person_with_different_shyness_level[i-1])
        if string_of_person_with_different_shyness_level[i] != 0:
            if no_of_persons < i:
                no_of_friends_to_invite = (i - no_of_persons) + no_of_friends_to_invite
                no_of_persons = no_of_persons + (i - no_of_persons)
        i = i+1
    return no_of_friends_to_invite
    
def write_result_in_file(count, no_of_friends_to_invite):
    fw = open(r'C:\Users\Krishna\Desktop\Google Code Jam 2015\Problem A Standing Ovation\Output.txt', 'a')
    fw.write("Case #" + str(count+1) + ": " + str(no_of_friends_to_invite))
    fw.write('\n')
    fw.close()
    return

#Open the file
f = open(r'C:\Users\Krishna\Desktop\Google Code Jam 2015\Problem A Standing Ovation\A-large.in', 'r')

#Get no. of test cases
no_of_test_case = int(f.readline())

#Exit with status 1
#if no_of_test_case < 0 and no_of_test_case > 100:
#    exit(1)

#Initialize counter for loop
count = 0
while count < no_of_test_case:
    #Get test case
    test_case = f.readline().rstrip('\n')
    
    #Get maximum shyness level
    max_shyness = int(test_case.split()[0])
    
    #Exit with status 1
    #if max_shyness < 0 and max_shyness > 1000:
    #    exit(1)
    
    #Get string with persons of different shyness level
    string_of_person_with_different_shyness_level = test_case.split()[1]

    #Exit with status 1
    #if len(string_of_person_with_different_shyness_level) != max_shyness+1:
    #    exit(1)

    #Exit with status 1
    #if string_of_person_with_different_shyness_level[max_shyness] == 0:
    #    exit(1)

    #Find no. of friends to invite
    no_of_friends_to_invite = find_no_of_friends_to_invite(max_shyness, string_of_person_with_different_shyness_level)
    
    #Write result in file
    write_result_in_file(count, no_of_friends_to_invite)
    
    #Increment loop counter
    count = count + 1

#Close the file
f.close()

#Exit with status 0
#exit(0)
