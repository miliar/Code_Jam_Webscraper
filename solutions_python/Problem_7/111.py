from math import *
from random import *


###################################################################
##################### Round 1B: Misc Funcions ######################
###################################################################


############### law_of_cosines  ###################################


def law_of_cosines(a, b, c):
    """ uses the law of cosines to return an angle using 3 triangle lengths """
    
    cos_gamma = (a**2 + b**2 - c**2) / (2*a*b)
    return acos(cos_gamma)*180/pi



###################################################################
##################### Round 1B: Problem A ##########################
###################################################################

def arrange_problem_a(word_list):
    """ arranges the data for problem_a """
    
    num_cases = int(word_list[0])
    arranged_list = []
    word_iter = 1
    
    for case in range(num_cases):
        new_case = []
        new_case = word_list[word_iter:word_iter+8]
        word_iter += 8    
    
    
        arranged_list.append(new_case)
        
    return arranged_list

def problem_a_main(arranged_message):
    """problem b's main computations"""
    
    case_num = 1
    for case in arranged_message:
        n = int(case[0])
        A = int(case[1])
        B = int(case[2])
        C = int(case[3])
        D = int(case[4])
        x0 = int(case[5])
        y0 = int(case[6])
        M = int(case[7])

        tree_coords = [[x0, y0]]
        for i in range(n-1):
            X = (A * x0 + B) % M
            Y = (C * y0 + D) % M
            x0 = X
            y0 = Y
            tree_coords.append([x0, y0])

        triangle_counter = 0
        for tree1 in tree_coords:
            tree_coords_without_tree1 = tree_coords[:]
            tree_coords_without_tree1.remove(tree1)
            for tree2 in tree_coords_without_tree1:
                tree_coords_without_tree2 = tree_coords_without_tree1[:]
                tree_coords_without_tree2.remove(tree2)
                for tree3 in tree_coords_without_tree2:
                    middle_x_coord = (tree1[0]+tree2[0]+tree3[0])/3.0
                    middle_y_coord = (tree1[1]+tree2[1]+tree3[1])/3.0
                    if middle_x_coord == floor(middle_x_coord) and middle_y_coord == floor(middle_y_coord):
                        triangle_counter += 1
                    

        print "Case #%s:" % case_num, triangle_counter/6
        case_num +=1





def problem_a(raw_string):
    problem_a_main(arrange_problem_a(raw_string.split()))


###################################################################
##################### Round 1B: Problem B ##########################
###################################################################

def arrange_problem_b(word_list):
    """ arranges the data for problem_b """
    
    num_cases = int(word_list[0])
    arranged_list = []
    word_iter = 1
    
    for case in range(num_cases):
        new_case = []


      
    
    
        arranged_list.append(new_case)
        
    return arranged_list




def problem_b_main(arranged_message):
    """problem a's main computations"""
    
    case_num = 1
    for case in arranged_message:


        print "Case #%s:" % case_num, "something"
        case_num +=1


def problem_b(raw_string):
    problem_b_main(arrange_problem_b(raw_string.split()))


###################################################################
##################### Round 1B: Problem C ##########################
###################################################################

def arrange_problem_c(word_list):
    """ arranges the data for problem_c """
    
    num_cases = int(word_list[0])
    arranged_list = []
    word_iter = 1
    
    for case in range(num_cases):
        new_case = []


      
    
    
        arranged_list.append(new_case)
        
    return arranged_list



def problem_c_main(arranged_message):
    """problem c's main computations"""
    
    case_num = 1
    for case in arranged_message:


        print "Case #%s:" % case_num, "something"
        case_num +=1



def problem_c(raw_string):
    problem_c_main(arrange_problem_c(raw_string.split()))
