f = open('B-large.in','r')
input_file = [x.strip().split() for x in f.readlines()]
f.close()

#number of cases
nC = int(input_file[0][0])

cases = []
for line in input_file[1:]:
    C,F,X = [float(x) for x in line]
    cases.append([C,F,X])
    

def solve_case(case):
    C,F,X = case
    R = 2
    clock_time = 0
    while True:
        time_to_break_even = C/R*(R+F)/F
        time_to_finish = X/R
        time_to_buy_a_farm = C/R
        
        if time_to_break_even < time_to_finish:
            clock_time = clock_time + time_to_buy_a_farm
            R = R + F
        else:
            clock_time = clock_time + time_to_finish
            break
    return clock_time

f = open('B_large_solution.txt','w')
for idx,case in enumerate(cases):
    solution = solve_case(case)
    f.write('Case #'+str(idx+1) + ': ' + str(solution) + '\n')

f.close()