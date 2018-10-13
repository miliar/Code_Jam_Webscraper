#/usr/bin/python
import sys
import itertools

def split_candies(candies):
    best_sum = 0
    for pile_size in range(1,len(candies)/2 + len(candies) % 2 + 1 ):
        for pile_1 in itertools.combinations(candies, pile_size):
            pile_2 = candies[:]
            for cand in pile_1:
                pile_2.remove(cand)
            if check_sums(pile_1,pile_2):
               max_sum = max(sum(pile_1), sum(pile_2))
               if max_sum > best_sum:
                    best_sum = max_sum
    return best_sum
        


def check_sums(pile_1, pile_2):
    sum_1 = None
    for candy in pile_1: 
        if sum_1 is None:
            sum_1 = candy
        else:
            sum_1 = add_numbers(sum_1, candy)
    sum_2 = None
    for candy in pile_2: 
        if sum_2 is None:
            sum_2 = candy
        else:
            sum_2 = add_numbers(sum_2, candy)
    
    return sum_1 == sum_2 


def add_numbers(num_1, num_2):
    nbin_1 = bin(num_1)[2:]
    nbin_2 = bin(num_2)[2:]
    if len(nbin_1) > len(nbin_2):
        nbin_2 = nbin_2.rjust(len(nbin_1), '0')
    if len(nbin_2) > len(nbin_1):
        nbin_1 = nbin_1.rjust(len(nbin_2), '0')

    result = []
    for i in range(len(nbin_1)):
        if nbin_1[i] == nbin_2[i]:
            result.append('0')
        else:
            result.append('1')
    return int("0b{0}".format(''.join(result)),2)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(1)
    infile = sys.argv[1]
    print infile
    with open(infile) as f:
        num_tests = int(f.readline())
        print "number of tests: {0}".format(num_tests)
        case_number = 1
        solutions = {}
        for i in range(num_tests):
            print "Solving case #{0}".format(case_number)            
            num_candies = int(f.readline())
            candies = []
            for candy in f.readline().split():
                candies.append(int(candy))
            
            sol = split_candies(candies)
            if sol:
                solutions[case_number] = sol
            else:
                solutions[case_number] = 'NO'
            case_number += 1

        
    outfile = sys.argv[2]
    with open(outfile, 'w') as of:
        for solution in solutions:
            of.write('Case #{0}: {1}\n'.format(solution, solutions[solution]))
