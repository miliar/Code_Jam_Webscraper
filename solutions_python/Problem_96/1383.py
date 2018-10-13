def solve(n, num_surprises, p, t_list):
    result = 0
    #print n, num_surprises, p, t_list

    if p > 0:
        threshold = p*3 - 2 #[p-1, p-1, p]
    else:
        threshold = 0

    if p == 1:
        return len([t for t in t_list if t >= 1])
    
    for t in reversed(sorted(t_list)):
        if t >= threshold:
            result += 1
        elif num_surprises > 0 and t >= threshold-2:
            result += 1
            num_surprises -= 1
        else:
            return result
        
    return result

#input, solve and output:
                        
input = open('B-small-attempt0.in', 'r')
output = open('B-small-attempt0.out', 'w')

num_cases = int(input.readline())
for case in range(1, num_cases+1):
    this_line = map(int, input.readline().strip().split())
    n, num_surprises, p = this_line[:3]
    t_list = this_line[3:]
    
    result = solve(n, num_surprises, p, t_list)
    #print result
    
    output.write('Case #%s: %s\n' %(case, result))

input.close()
output.close()

