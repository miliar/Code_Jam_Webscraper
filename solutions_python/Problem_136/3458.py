f=open('B-small.in','r')
fo=open('B-small.out','w')
total_test_cases = int(f.readline().strip('\n'))
test_case_count = 1

e = f.readline()
while (test_case_count <= total_test_cases):
    s_line = e.strip('\n')
	
    n_time = float("0.0000000")
    n_sum = float("0.0000000")
    lst_time_n = []
    lst_time_sum = []
    n_rate = float("2.0000000")
    is_stop = False
    
    (C, F, X) = s_line.split()
    (n_C, n_F, n_X) = (float(C), float(F), float(X))
    
    while is_stop == False:
        lst_time_n.append(n_C/n_rate)
        n_sum = sum(lst_time_n[:-1]) + (n_X/n_rate)
        lst_time_sum.append(n_sum)
        n_rate += n_F

        if sum(lst_time_sum) <=1 or min(lst_time_sum)!=lst_time_sum[-1]:
            is_stop=True

    if len(lst_time_sum)>1:
        n_min_time = lst_time_sum[-2]
    else:
        n_min_time = lst_time_sum[-1]
    
    s_answer = "%0.7f" % (n_min_time)
	
    fo.write('Case #'+ str(test_case_count)+ ': '+ s_answer + '\n')
    test_case_count = test_case_count + 1
  
    e = f.readline()
    if (not e):
        break

f.close()
fo.close()
