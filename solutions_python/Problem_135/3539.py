f=open('A-small.in','r')
fo=open('A-small.out','w')

total_test_cases = int(f.readline().strip('\n'))
test_case_count = 1

e = f.readline()
while (test_case_count <= total_test_cases):
    n_first_ans = int(e.strip('\n'))
    lst_first_ans = []
    lst_second_ans = []
    
    i = 1
    while i <= 4:
            se = f.readline().strip('\n');
            if n_first_ans==i:
                    lst_first_ans = se.split()
            i += 1
    
    n_second_ans = int(f.readline().strip('\n'))
    j = 1
    while j <= 4:
            se = f.readline().strip('\n');
            if n_second_ans==j:
                    lst_second_ans = se.split()
            j += 1
    
    s_answer = ''
    join_result = set(lst_first_ans).intersection(lst_second_ans)
    count_element = len(join_result)
    if count_element==1:
            s_answer = join_result.pop()
    elif count_element > 1:
            s_answer ='Bad magician!'
    else:	
            s_answer = 'Volunteer cheated!'

    
    fo.write('Case #'+ str(test_case_count)+ ': '+ s_answer + '\n')
    test_case_count = test_case_count + 1
  
    e = f.readline()
    if (not e):
        break

f.close()
fo.close()
print 'Done!'
