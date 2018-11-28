##input = open('B-sample-input.txt', 'r')
##output = open('B-sample-output.txt', 'w')

input = open('B-small-attempt1.in', 'r')
output = open('B-small.out', 'w')

##input = open('B-large-practice.in', 'r')
##output = open('B-large.out', 'w')

def read_int():
    return int(input.readline().strip())

def read_ints():
    return [int(x) for x in input.readline().split()]

def read_float():
    return float(input.readline().strip())

def read_floats():
    return [float(x) for x in input.readline().split()]

def solve(ac, aj, acs, ajs):
##    print ac, aj
##    print acs
##    print ajs
    if ac == 0:
        ajs.sort()
        if aj == 1:
            return 2
##        print ajs
        if ajs[0][0] + 720 >= ajs[1][1]:
##            print 'here'
            return 2
        elif ajs[1][0] + 720 >= ajs[0][1] + 1440:
##            print 'here2'
            return 2
        else:
            return 4
    if aj == 0:
        acs.sort()
        if ac == 1:
            return 2
        acs.sort()
##        print acs
        if acs[0][0] + 720 >= acs[1][1]:
##            print 'here'
            return 2
        elif acs[1][0] + 720 >= acs[0][1] + 1440:
##            print 'here2'
            return 2
        else:
            return 4
    if ac == 1 and aj == 1:
        return 2
    return

def main():
    num_cases = read_int()
    for case in range(1, num_cases+1):
        ac, aj = read_ints()
        acs = []
        ajs = []
        for i in range(ac):
            acs.append(read_ints())
        for i in range(aj):
            ajs.append(read_ints())
##        if case == 23:        
        solution = solve(ac, aj, acs, ajs)
        solution_string = "Case #%d: %s" %(case, solution)
        output.write(solution_string + "\n")
        print solution_string
        

main()
input.close()
output.close()
    
