import sys

#input = open('test.in')
input = open('A-large.in')
#output = sys.stdout
output = open('A-large.out','w')
    
def myread():
    return input.readline().rstrip("\n\r")

def int_ize(an_array):
    return map(lambda x: int(x), an_array)

def main():
    n_cases = int(input.readline())
    
    case_no = 1
    while case_no <= n_cases:
        case_result = solve_case()
        output.write("Case #%d: %s\n" % (case_no, case_result))
        case_no+=1
    
def solve_case():
    (n,k) = int_ize(myread().split(" "))
    if (k % 2**n) == (2**n - 1):
        return "ON"
    else:
        return "OFF"

main()
