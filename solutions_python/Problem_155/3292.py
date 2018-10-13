__author__ = 'javierfdr'
# Javier Fernandez Google Code Jam 2013
# Google Code Jam 2013
# javierfdr@gmail.com - javierfdr
# Standing Ovation

import sys

def calculateNumInvitations(audience,max_shy):

    all_but_last = audience
    sum = 0
    index = 0;
    extra = 0
    current_remaining = 0
    for i in all_but_last:
        current_remaining = 0
        value = int(i)
        if(index==0):
            index = index+1
            sum = sum+value
            continue

        if (sum<index):
            current_remaining = index-sum

        extra = extra+current_remaining
        sum = sum+value+current_remaining

        index = index+1

    return extra


out_file = open('output.out','w+')
#in_file = sys.stdin
in_file = open('a-large1.in')
num_cases = int(in_file.readline())
for c in range(1,num_cases+1):
    case = 'Case #'+str(c)+': '

    input_string = in_file.readline().split(' ')
    max_shy = input_string[0]
    audience = input_string[1].strip('\n')

    result = case+str(calculateNumInvitations(audience,int(max_shy)))+'\n'
    out_file.write(result)