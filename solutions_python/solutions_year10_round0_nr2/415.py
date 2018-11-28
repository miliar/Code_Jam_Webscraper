## -------------------------------------------

def parse_file(filename):
    lines = file(filename,'r').read().splitlines()
    counter = 0
    n_cases = map(int, lines[counter].strip().split())[0]
    counter += 1
    cases = []

    for n_case in xrange(n_cases):
        x = map(int, lines[counter].strip().split())
        cases.append(x[1:])
        counter += 1

    return cases


def gcd(a,b):
    while b:
        a,b = b, a%b
    return a


def solve_case(nums):
    n = len(nums)
    common = 0
    for i in range(n):
        for j in range(i+1,n):
            common = gcd(common, abs(nums[i]-nums[j]))
            
    shift = [(common-(nums[i]%common))%common for i in range(n)]
    assert len(set(shift)) == 1    
    return shift[0]
        
        
    
def print_solution(case_number, sol, outfile):
    outfile.write("Case #%d: %d\n" % (case_number+1, sol))
    
    
def solve(filename, outfilename):
    cases = parse_file(filename)
    outfile = file(outfilename,'w')
    
    for i, x in enumerate(cases):
        print "%d/%d" % (i+1, len(cases))
        n = solve_case(x)
        print_solution(i, n, outfile)