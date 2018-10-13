'''
Created on 14 Apr 2012

@author: manofest
'''
import os
import math

folder = 'A2'
input_file_name = 'B-small-attempt1.in' 
output_file_name = 'B-small-attempt1.out'


def diff(n1,n2): 
    ans = (int(n1) - int(n2))
    return ans

def Process(input_file):
    output = open(folder + os.sep + output_file_name,'wb')
    
    total = input_file.readline().strip()

    #results = []
    case = 1
    print "Processing and writing out file"
    for line in input_file:
        #print "line"
        totalS = 0
        record_count = 0
        record = line.split()
        N = record[0]
        S = record[1]
        p = record[2]
        scores = record[3:]
        count_special = 0
        for score in scores:
            if int(case) == 82:
                print score
            score_list2 = []
            #print "For Score " + str(score)
            import itertools
            new_list = []
            for j in range(3):
                for i in range(int(int(score))):
                    new_list.append(i)
          
            combos =  list(itertools.combinations(new_list, 3))
           
            for i in combos:
                one_two = False
                one = False
                if sum(i) == int(score):
                    diff_combos = list(itertools.combinations(i, 2))
#                    i1, i2 = diff_combos
                    for j in diff_combos:
                        n1, n2 = j
                        the_diff = abs(diff(int(n1),int(n2)))
                        if int(case) == 82:
                            print the_diff
                        if int(the_diff) <= 2:
                            if one_two == False and int(the_diff) == 2 :
                                one_two = True
                            elif int(the_diff) == 1:
                                one = True
                            elif int(the_diff) == 0:
                                one = True
                        else:
                            one = False
                            one_two = False
                            break
                    if one == True or (one == True and one_two == True):
                        
                        l1,l2,l3 = i
                        res = [int(l1),int(l2),int(l3)]
                        res.sort()
                        
                        if (one == True and one_two == True):
                            if [res,True] not in score_list2:
                                if int(case) == 82:
                                    print res
                                score_list2.append([res,True])
                        else:
                            if [res,False] not in score_list2:
                                if int(case) == 82:
                                    print res
                                score_list2.append([res,False])
            sdfsfd = False
            if int(p) == 0:
                record_count = record_count + 1
            else:
                for resout in score_list2:
                    if sdfsfd == False:
                        for num in resout[0]:
                            if int(case) == 82:
                                print "The value for p is " + str(p)
                                print "the nu mis " + str(num)
                            if bool(resout[1]) == False:
                                if (int(num)) >= int(p):
                                    if int(case) == 82:
                                        print resout[0]
                                    record_count = record_count + 1
                                    sdfsfd = True
                                    break
                
                if sdfsfd == False and ((int(count_special) < int(S) and int(S) != 0)):
                    for resout in score_list2:
                        if sdfsfd == False:
                            for num in resout[0]:
                                if bool(resout[1]) == True:
                                    if (int(num)) >= int(p):
                                        if int(case) == 82:
                                            print resout[0]
                                        record_count = record_count + 1
                                        sdfsfd = True
                                        count_special = count_special + 1
                                        break
        print case                
        output.write("Case #" + str(case) + ": " + str(record_count) + "\n")
        case = case + 1
    
    output.close()


if __name__ == '__main__':
    
    print "Starting"
    input_file = open(folder + os.sep + input_file_name)
    Process(input_file)
    
    input_file.close()
    print "Finished Processing"