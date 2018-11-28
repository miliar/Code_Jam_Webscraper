'''
Created on Apr 12, 2014

@author: ankits
'''

def run(case_no, first_row_ans, second_row_ans):
    first_row_ans = first_row_ans.split('\n')[0]
    second_row_ans = second_row_ans.split('\n')[0]
    
    first_set = set(first_row_ans.split(' '))
    second_set = set(second_row_ans.split(' '))
    
    res_set = first_set & second_set
    res_len = len(res_set) 
    if res_len == 1:
        print 'Case #{0}: {1}'.format(case_no, res_set.pop())
    elif res_len == 0:
        print 'Case #{0}: {1}'.format(case_no, 'Volunteer cheated!')
    else:
        print 'Case #{0}: {1}'.format(case_no, 'Bad magician!')

f = open('A-small-attempt1.in')
no_of_test_case =  f.readline()

for i in xrange(int(no_of_test_case)):
    first_row = f.readline()
    for index in xrange(4):
        row = f.readline()
        if index == int(first_row)-1:
            first_row_ans = row
                
    second_row = f.readline()
    for index in xrange(4):
        row = f.readline()
        if index == int(second_row)-1:
            second_row_ans = row
            
    run( i+1,first_row_ans, second_row_ans)
         
