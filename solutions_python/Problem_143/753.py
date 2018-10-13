##input = open('C-sample-input.txt', 'r')
##output = open('C-sample-output.txt', 'w')
input = open('/Users/pruthvikarreddy/Downloads/B-small-attempt0 (1).in', 'r')


#input = open('C-small-attempt3.in', 'r')
output = open('/Users/pruthvikarreddy/Downloads/B-small.out', 'w')

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
    
def read_floats():
    return [float(x) for x in input.readline().split()]
    
def read_strs():
    return [x for x in input.readline().split()]

def read_str():
    return input.readline().strip()
    
def read_floats():
    return input.readline().split()

def solve(N, perm):
    return 'ans'


def af(a,b):
    return a&b
    
def main():
    num_cases = read_int()
    for case in range(1, num_cases+1):
        A,B,K=read_ints()
        c=0
        for a in xrange(A):
            for b in xrange(B):
                if af(a,b)<K:
                    c+=1
        solution=c
        solution_string = "Case #%d: %s" %(case, solution)
        output.write(solution_string + "\n")
        print solution_string
        
if __name__=='__main__':
    main()
    input.close()
    output.close()
    
