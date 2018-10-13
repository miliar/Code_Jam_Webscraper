
import time


_problem = 'A'
_size = 'large'
_size = 'small'

input_file = _problem + '-' + _size + '.in'
input_file = 'A-small-attempt0.in'

output_file = input_file + '.txt'

DEBUG = True
DEBUG = (_size == 'small')
def dummy(*args, **kwargs):
    pass
debug = print if DEBUG else dummy

        
def process_cases(input_file, output_file):
    with open(input_file, 'r') as fin, open(output_file, 'w') as fout:
        nr_cases = int(fin.readline())
        print('--> Test cases: %d' % nr_cases)
        for c in range(nr_cases):
            if c % 100 == 0: 
                print('--> %d' % (c + 1))
            else:
                debug('--> %d' % (c + 1))
            result = solve_case(fin)
            debug(result)
            fout.write('Case #%d: %s\n' % (c + 1, str(result)))

#----------------------------------------------------------------------------------------------------------------------            
    
def solve_case(file):
    row1 = int(file.readline())
    arr1 = list()
    for i in range(4):
        line = file.readline().strip()
        if (i + 1) == row1:
            set1 = set(map(int, line.split()))
    row2 = int(file.readline())
    arr2 = list()
    for i in range(4):
        line = file.readline().strip()
        if (i + 1) == row2:
            set2 = set(map(int, line.split()))
    cards = set1 & set2
    if len(cards) > 1:
        return 'Bad magician!'
    if len(cards) == 0:
        return 'Volunteer cheated!'
    return cards.pop()

#----------------------------------------------------------------------------------------------------------------------            
    
if __name__ == "__main__":
    start_time = time.perf_counter()
    process_cases(input_file, output_file)
    print('--> Total time: %.2f' % (time.perf_counter() - start_time))