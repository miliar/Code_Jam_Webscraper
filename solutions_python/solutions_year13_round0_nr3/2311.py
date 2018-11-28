import math


def fair_and_square(A, B):
    count = 0
    sqrt_A = int(math.ceil(math.sqrt(A)))
    sqrt_B = int(math.floor(math.sqrt(B)))

    for x in range(sqrt_A, sqrt_B+1):

        if check_palindromes(x) and check_palindromes(x**2):
#            print x**2
            count += 1
#    print count
    return count





def check_palindromes(x):
    cand = str(x)
    reverse_cand = cand[::-1]
    if cand == reverse_cand:
        return True
    else:
        return False


def output_file(outcome, filename):
    f = open(filename, 'w')
    for x, y in outcome:
        print x,y
        f.write("Case #%d: %d\n"%(x,y))
    f.close()

def read_input(filename):
    f = open(filename)
    num_of_cases = int(f.readline())
    cases = []

    for i in range(num_of_cases):
        A,B = f.readline().split()
        cases.append([int(A),int(B)])

#    print cases
    f.close()

    return cases


if __name__ == '__main__':
    cases = read_input('./input/C-small-attempt0.in')
    outcome = []
    for cid in range(len(cases)):
        case = cases[cid]
        count = fair_and_square(case[0], case[1])
        outcome.append([cid+1, count])

    output_file(outcome, './input/C-small-attempt0.out')
