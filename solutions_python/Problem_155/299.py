def solve(case_string):
    result = 0
    
    s_max, s_string = case_string.split()
    s_max = int(s_max)
    s_string = [int(num) for num in s_string]

    #print s_max, s_string

    sum_k_1 = 0
    for k, num in enumerate(s_string):
        
        if sum_k_1 + result < k:
            result += (k - sum_k_1 -result)

        #print k, num, ' ', sum_k_1 + result, '=', sum_k_1, '+', result

        sum_k_1 += num
    #print
    
    return result

#input, solve and output:
                        
input = open('A-large.in', 'r')
output = open('A-large.out', 'w')

num_cases = int(input.readline())
for case in range(1, num_cases+1):
        #no strip, in case get rid of -1, in case ' ' in the front
        case_string = input.readline().strip()
        result = solve(case_string)

        result_string = 'Case #%s: %s\n' %(case, result)
        #print result_string
        output.write(result_string)

input.close()
output.close()
