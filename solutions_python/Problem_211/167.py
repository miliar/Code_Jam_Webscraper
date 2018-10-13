##input = open('C-sample-input.txt', 'r')
##output = open('C-sample-output.txt', 'w')

input = open('C-small-1-attempt0.in', 'r')
output = open('C-small.out', 'w')

##input = open('C-large.in', 'r')
##output = open('C-large.out', 'w')

def read_int():
    return int(input.readline().strip())

def read_ints():
    return [int(x) for x in input.readline().split()]

def read_float():
    return float(input.readline().strip())

def read_floats():
    return [float(x) for x in input.readline().split()]

def solve(n, k, u, ps):
    ps.sort()
    ps.append(1)
##    print ps
    i = 0
    while u > 0:
##        print 'i', i
##        print 'u', u
        current_total = sum(ps[:i+1])
        needed = ps[i+1] * (i+1)
##        print 'current', current_total
##        print 'needed', needed
        if u >= needed - current_total:
            for j in range(i+1):
                ps[j] = ps[i+1]
            u -= (needed - current_total)
        else:
            increment = u / (i+1)
            for j in range(i+1):
                ps[j] += increment
            u -= (increment * (i+1))
        i += 1
    total = 1
    for i in range(n):
        total *= ps[i]
    return total
        

def main():
    num_cases = read_int()
    for case in range(1, num_cases+1):
        n, k = read_ints()
        u = read_float()
        ps = read_floats()
##        if case == 4:        
        solution = solve(n, k, u, ps)
        solution_string = "Case #%d: %s" %(case, solution)
        output.write(solution_string + "\n")
        print solution_string
        

main()
input.close()
output.close()
    
