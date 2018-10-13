##input = open('A-sample-input.txt', 'r')
##output = open('A-sample-output.txt', 'w')

##input = open('A-small-attempt0.in', 'r')
##output = open('A-small.out', 'w')

input = open('A-large.in', 'r')
output = open('A-large.out', 'w')

def read_int():
    return int(input.readline().strip())

def read_ints():
    return [int(x) for x in input.readline().split()]

def read_float():
    return float(input.readline().strip())

def read_floats():
    return [float(x) for x in input.readline().split()]

def solve(s, k):
    s = [x for x in s]
    count = 0
##    print "".join(s)
    for i in range(len(s) - k + 1):
##        print 'i=', i
        if i == len(s) - k:
            pluses = 0
            minuses = 0
            for j in range(i, len(s)):
                if s[j] == "+":
                    pluses += 1
                else:
                    minuses += 1
            if pluses == k:
                return count
            if minuses == k:
                return count + 1
            else:
                return "IMPOSSIBLE"
        if s[i] == "-":
            count += 1
            for j in range(i, i + k):
                if s[j] == "-":
                    s[j] = "+"
                else:
                    s[j] = "-"


def read_data():
    x = input.readline().split()
    s = x[0]
    k = int(x[1])
    return s, k
    

def main():
    num_cases = read_int()
    for case in range(1, num_cases+1):
        s, k = read_data()
##        if case == 4:        
        solution = solve(s, k)
        solution_string = "Case #%d: %s" %(case, solution)
        output.write(solution_string + "\n")
        print solution_string
        

main()
input.close()
output.close()
    
