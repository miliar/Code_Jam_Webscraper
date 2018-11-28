def pairs(num):
    l = len(num)
    return set(num[-i:]+num[:l-i] for i in xrange(1, len(num)))-set([num])

def solve_case(A, B):
    num_of_pairs = 0
    numbers = [str(num) for num in xrange(int(A), int(B)+1)]
    while numbers:
        number = numbers.pop(0)
        pairs_of_number = pairs(number)
        for pair in pairs_of_number:
            if pair[0] != '0' and pair>=A and pair<=B and pair<number:
                num_of_pairs += 1
    return num_of_pairs

def solve(filename, out_filename):
    with open(filename) as in_file:
        with open(out_filename, 'wb') as out_file:
            cases = int(in_file.next().strip())
            for i in xrange(cases):
                line = in_file.next().strip()
                out_file.write('Case #%d: %s\r\n' % (i+1, solve_case(*line.split(' '))))

if __name__ == '__main__':
    solve('C-small-attempt0.in', 'C-small-attempt0.out.txt')
    
