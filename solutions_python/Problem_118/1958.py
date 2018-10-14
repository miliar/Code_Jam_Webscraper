#!/usr/bin/env python

###### Modules ######
import os
import math
import string
import sys
import itertools
#####################

##########################################################################
working_dir = "C:\Users\MyPC\Documents\codejam_2013\Fair_and_Square_qual_2013\\"
#input_file = "B-small-attempt2-chk.in"
#output_file = "B-small-attempt2-chk.out"

input_file = "C-small-attempt0.in"
output_file = "C-small-attempt0.out"
junk_file = "junk.txt"
##########################################################################

#***************************************************************
def Grab_Input_File(working_dir, input_file):
    """ Input: working directory and input file name.
        Output: open input file and return file object. """
    abs_in_file_path = working_dir + input_file
    try:
        f = open(abs_in_file_path, 'rU')
    except IOError:
        print "Error: File not found"
        return 0
    return f
#****************************************************************
def Get_One_Test_Case(in_file):
    """ Extract one test case from the input file and
        put it in appropriate data structure.
        Input: file object, Output: a data structure containing single test case."""
    (A, B) = (in_file.readline()).split()
    A = int(A)
    B = int(B)
    return [A, B]
#****************************************************************
def Make_Palindromes(count):
    """Returns list of palindromes from length=1 to count. """
    p_list = []
    Lmax = count
    for cnt in range(Lmax):
        L = cnt
        pal = 'x'*L
        var_count = int(math.ceil(float(L)/2))
        E = []
        for i in range(var_count):
            E.append[range(10)]
            for j in range(10):
                if i == 0:
                    if j!= 0:
                        pal[i] = str(j)
                        pal[L-1-i] = str(j)
                else:
                    pal[i] = str(j)
                    pal[L-1-i] = str(j)
        p_list.append(pal)    
    return p_list
#***************************************************************
#****************************************************************
def Make_Palindromes2(count):
    """Returns list of palindromes from length=1 to count. """
    p_list = []
    Lmax = count
    print "Lmax=", Lmax
    for cnt in range(Lmax):
        L = cnt+1
        if L == 1:
            for q in range(1,10):
                p_list.append(str(q))
            continue
        elif L == 2:
            for q in range(1,10):
                p_list.append((str(q)+str(q)))
            continue
                
        else:
            pal = ''
            rev_pal = ''
            var_count = int(math.ceil(float(L)/2))
            E = range(10)
            X = range(1,10)
            prod_count = var_count-1
            if prod_count == 0:
                Z1 = [p for p in itertools.product(X, repeat=1)]
                Z2 = [p for p in itertools.product(X, Z1)]
                prod_count = 1
            else:
                Z1 = [p for p in itertools.product(E, repeat=(prod_count))]
                Z2 = [p for p in itertools.product(X, Z1)]
            #print Z2
            #print "$$$$$$$$$$$$$$$$$$$$$$$$"
            for element in Z2:
                pal = ''
                rev_pal = ''
                #print element
                pal+=str(element[0])
                #print prod_count
                #print "var_count = ", var_count
                #print pal
                #print "@@@@@@@@@@@@@@@@@@"
                #print element
                #print "@@@@@@@@@@@@@@@@@@"
                #print "prod count", prod_count
                for index in range(prod_count):
                    pal+=str(element[1][index])
                    #print index
                    #print "XXXXXXX"
                    #try:
                    #    print pal
                    #except MemoryError:
                    #    print "Mem error occured"
                    #    print "element = ", element
                    #    sys.exit(1)
                rev_pal = pal[::-1]
                #rev_pal = ''
                #print pal
                #print rev_pal
                #print "L is: ", L
                if L%2 != 0:
                    pal = pal[:-1]+rev_pal
                else:
                    pal = pal+rev_pal
                p_list.append(pal)    
    return p_list
#***************************************************************
#****************************************************************
def Check_Palindrome(N):
    """Returns True if palindrome else False """
    S = str(N)
    if S == S[::-1]:
        return "True"
    else:
        return "False"
    
    L = len(S)
    p_flag = "True"
    for count in range(int(math.ceil(float(L)/2))):
        if S[L-1-count]!=S[count]:
            p_flag = "False"
            break
    return p_flag
#***************************************************************
#****************************************************************
def Square(N):
    N = int(N)
    """Returns square of the number. """
    return str(N*N)
#***************************************************************
def Compute_Result(test_case):
    """ Grab a single testcase, perform computation and return the result."""
    A = test_case[0]
    B = test_case[1]
    N = int(math.floor(pow(B,0.5)))
    print A, B, N
    p_count = 0
    pal_list = Make_Palindromes2(len(str(N)))
    #print "in compute result section"
    print pal_list
    J = open((working_dir+junk_file), 'w')
    for elem in pal_list:
        esq = Square(elem)
        #print "elem = ", elem, "and its square is: ", esq
        tmp = Check_Palindrome(esq)
        txt = str(elem)+" "+str(esq)+"\n"
        J.write(txt)
        if tmp=="True":
            print esq, "is a palindrome"
            if (int(esq)>=int(A)) and (int(esq)<=int(B)):
                p_count+=1
        else:
            zasa = 1#print esq, "is not a palindrome"
    J.close()
    #sys.exit(1)
    return str(p_count)
        

#***************************************************************
def Save_And_Display_Results(results, output_file):
    """ Save the results into a specified output file and
        display the results on the screen."""
    def Format_Result(case_index, result):
        """ Returns the result transformed into one big string with
            new lines inserted at appropriate places. This string
            can be directly written into a file and also printed
            directly to screen."""
        ### Code to transform result into one big string.
        formatted_result = 'Case #' + str(case_index) + ': ' + result
        return formatted_result
    
    f = open(output_file, 'w')
    for case_index in sorted(results.keys()):
        formatted_result_to_screen = Format_Result(case_index, results[case_index])
        formatted_result_to_file = formatted_result_to_screen + '\n'
        f.write(formatted_result_to_file)
        print '***************************************'
        print formatted_result_to_screen
    print '***************************************'
    
#***************************************************************
def main():
    f = Grab_Input_File(working_dir, input_file)
    # Extract the number of test cases.
    T = int(f.readline())
    #print T
    #sys.exit(1)
    # dictionary to store result of computation. Key = testcase#
    results ={}
    for index in range(T):
        case_index = index + 1
        test_case = Get_One_Test_Case(f)
        #print test_case
        #print '*************************************'
        results[case_index] = Compute_Result(test_case)
    print "T = ", T
    abs_out_file_path = working_dir + output_file
    #sys.exit(1)
    Save_And_Display_Results(results, abs_out_file_path)
    f.close()

#***************************************************************
if __name__ == '__main__':
    main()
    