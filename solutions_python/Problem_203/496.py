import random
import sys
import os
import time
import math
import argparse
import numpy
import threading


#return [-1,-1] if check_done is true
#return [i, index of ?] if false
def check_done(arr):
    for i in range(0, len(arr)):
        x = arr[i]
        if ("?" in x):
            ind = x.find('?')
            return [i, ind]
    return [-1,-1]



def gen_questions(n):
    s = ""
    for i in range(0,n):
        s = s+"?"
    return s


def findfirst(s):

    i = 0
    s = list(s)
    letter = ""

    while(s[i] == "?"):
        i = i+1
    letter = s[i]

    #j is index of first letter in original
    j = i


    while (i >= 0):
        if(s[i] == "?"):
            s[i] = letter
        i = i-1

    i = j

    while (i < len(s)):
        if (s[i] == "?"):
            s[i] = letter
        else:
            letter = s[i]
        i = i+1

    return ''.join(s)


def solve(arr):

    R = len(arr)
    C = len(arr[0])
    questions = gen_questions(C)

    for i in range(0, R):
        if (arr[i] == questions):
            continue
        else:
            arr[i] = findfirst(arr[i])

    j = 0
    for i in range(0,R):
        if (arr[i] == questions):
            continue
        else:
            j = i
            break

    #j is index of first non question mark string
    rep = arr[j]

    k = j


    while (j >= 0):
        if(arr[j] == questions):
            arr[j] = rep
        j = j-1

    j = k

    while (j < len(arr)):
        if (arr[j] == questions):
            arr[j] = rep
        else:
            rep = arr[j]
        j = j+1

    return arr



    #tuple = check_done(arr)
    #while (not (tuple[0] == -1)):
        #ind1 = tuple[0]
        #look_at = arr[ind1]

        #tuple = check_done(arr)



def input():
    g = open("large.in")
    inp = g.read()
    input_arr = inp.splitlines()
    num_inputs = int(input_arr[0])
    del input_arr[0]

    org = sys.stdout
    f = open('output_large.txt', 'w')
    sys.stdout = f


    for i in range (0, num_inputs):
        curr_nums = input_arr[0].split()
        num_lines = int(curr_nums[0])
        num_chars = int(curr_nums[1])
        curr_list = input_arr[1:(num_lines+1)]
        input_arr = input_arr[(num_lines+1):]
        #print(check_done(curr_list))
        #print(curr_list)
        #print(solve(curr_list))
        arr = solve(curr_list)
        print "Case #%d:" % (i+1)
        for j in range(0, len(arr)):
            print arr[j]




    #print input_arr


    sys.stdout = org
    f.close()

input()