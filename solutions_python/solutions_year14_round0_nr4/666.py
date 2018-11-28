##input = open('D-sample-input.txt', 'r')
##output = open('D-sample-output.txt', 'w')

##input = open('D-small-attempt1.in', 'r')
##output = open('D-small.out', 'w')

input = open('D-large.in', 'r')
output = open('D-large.out', 'w')

def read_int():
    return int(input.readline().strip())

def read_ints():
    return [int(x) for x in input.readline().split()]

def read_float():
    return float(input.readline().strip())

def read_floats():
    return [float(x) for x in input.readline().split()]

def solve(blocks, naomi, ken):
    naomi.sort()
    ken.sort()
##    print naomi
##    print ken
    pcheat = 0
    j = 0
    for i in range(len(naomi)):
        if naomi[i] > ken[j]:
            pcheat += 1
            j += 1
    i = 0
    j = 0
    pnocheat = 0
    while j < len(naomi):
        while j < len(naomi) and ken[j] < naomi[i]:
            j += 1
        if j < len(naomi):
            pnocheat += 1
        i += 1
        j += 1
    return str(pcheat)+ " " + str(len(naomi) - pnocheat)
            
        

def main():
    num_cases = read_int()
    for case in range(1, num_cases+1):
        blocks = read_int()
        naomi = read_floats()
        ken = read_floats()
##        if case == 42:
        solution = solve(blocks, naomi, ken)
        solution_string = "Case #%d: %s" %(case, solution)
        output.write(solution_string + "\n")
        print solution_string
        

main()
input.close()
output.close()
    
