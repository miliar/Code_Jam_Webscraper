from math import *

#input_file = open('../test_input.txt','r')
input_file = open('A-small-attempt3.in','r')
raw_input = input_file.read()
input_file.close()

lines = raw_input.split('\n')

num_cases = int(lines[0])
case_num = 1

output_text = ''
output_file = open('consonants_output.txt','w')

case_start_line = 1

def isConsonant(c):
    if len(c)!=1:
        raise NameError("isConsonant of more than one char")
    else:
        if c in ['a','e','i','o','u']:
            return 0
        return 1

def uniques(L):
    seen = set()
    return [x for x in L if x not in seen and not seen.add(x)]

##case_num=5
##case_start_line=5
##while case_num<=5:
while case_num<=num_cases:
    s,n = (z for z in lines[case_start_line].split(' '))
    n = int(n)
    L=len(s)

    n_value = 0
    if n>L:
        n_value=0
##    elif n==L:
##        n_value=1
    else:
        is_cons_list = [None]*L
        for i in range(L):
            is_cons_list[i]=isConsonant(s[i])
            
        cons_thru = [None]*L
        cons_thru[0]=is_cons_list[0]
        for i in range(1,L):
            cons_thru[i] = is_cons_list[i] * (cons_thru[i-1]+1)
            
        is_start = [None]*(L-n+1)
        for i in range(len(is_start)):
            is_start[i] = (cons_thru[i+n-1]>=n)

        last_start = [-1]*L #index of last cons_thru[i]>=n
        i=0
        while i<len(is_start):
            if is_start[i]:
                last_start[i+n:L] = [i]*(L-n-i)
            i+=1

        if case_num==75:
            print(cons_thru)
            print(last_start)
        for i in range(L):
            if cons_thru[i]>=n:
                if case_num==75:
                    print(i-n-last_start[i]+1)
                    print(L-i)
                n_value += (i-n-last_start[i]+1)*(L-i)
    
    output_text = output_text+'Case #'+str(case_num)+': '+str(n_value)+'\n'

    case_start_line += 1
    case_num += 1

output_file.write(output_text)
output_file.close()
print(output_text)
