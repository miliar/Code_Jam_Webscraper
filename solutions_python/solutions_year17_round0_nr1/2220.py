'''
Created on Feb 22, 2017

@author: cturkarslan
'''
###REDIRECT IO
import sys
import re

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output_1.txt', 'w')


# sys.stdin = open('C-large-practice.in' ,'r')
# sys.stdout = open('output_2.txt' , 'w')

flip = {"-":"+","+":"-"}

def flip_fun(x): return flip[x]

T = int(input())
for i in range(T):
    pancake_str,K = input().split()
#    print("{} {}".format( pancake_str,K))
    K = int(K)
    state,count = "-",0
    j = 0
    while j + K - 1 < len(pancake_str):
        cur_idx = pancake_str.find("-",j)
        if(cur_idx == -1 or cur_idx + K > len(pancake_str)): break
        else:
           cur_substr = pancake_str[cur_idx:cur_idx + K]
#           print ("curr_substr: {}".format(cur_substr))
           new_substr = "".join(map(flip_fun,list(cur_substr)))
           pancake_str = pancake_str.replace(cur_substr,new_substr,1)
           count += 1
           j += 1
#        print("{} {}".format(pancake_str, count))
    if(pancake_str.find("-") == -1):  answer = count
    else: answer = "IMPOSSIBLE"



    # while j + K - 1 < len(pancake_str):
    #     cur_idx = pancake_str.find(state,j)
    #     if (cur_idx == -1):
    #         if(state == "-"):answer = count
    #         if(state == "+"):answer = "IMPOSSIBLE"
    #     else:   # Flip
    #         print("Flipping {}".format(cur_idx))
    #         count += 1
    #         if(cur_idx + K > len(pancake_str)):
    #             answer = "IMPOSSIBLE"
    #             break  # IMPOSSIBLE to flip
    #         next_idx = pancake_str.find(flip[state],cur_idx,cur_idx + K - 1)
    #         if(next_idx == -1):
    #             print(cur_idx)
    #             j = cur_idx + K
    #         else:
    #
    #             j = next_idx
    #             state = flip[state]
#    print("{} {}".format( pancake_str,K))
    print("Case #%d:" % (i + 1),answer)

if __name__ == '__main__':
    pass