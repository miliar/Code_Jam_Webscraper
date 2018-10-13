
import time
import random


_problem = 'B'
_size = 'large'
#_size = 'small'

input_file = _problem + '-' + _size + '.in'
#input_file = _problem + '.txt'

output_file = input_file + '.txt'

DEBUG = True
#DEBUG = (_size == 'small')
def dummy(*args, **kwargs):
    pass
debug = print if DEBUG else dummy

        
def process_cases(input_file, output_file):
    with open(input_file, 'r') as fin, open(output_file, 'w') as fout:
        nr_cases = int(fin.readline())
        #nr_cases = 100
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
    farm_cost, bonus, target = list(map(float, file.readline().strip().split()))
    #farm_cost, bonus, target = random.uniform(1, 10000), random.uniform(1, 100), random.uniform(1, 100000)
    #print((farm_cost, bonus, target))
    farm_delay = 0
    rate = 2.0
    time_old = target / rate
    while True:
        farm_delay += farm_cost / rate
        #debug('buy farm at %.7f' % farm_delay)
        time_new = farm_delay + target / (rate + bonus)
        if time_new > time_old:
            return time_old
        time_old = time_new
        rate += bonus
    return False

#----------------------------------------------------------------------------------------------------------------------            
    
if __name__ == "__main__":
    start_time = time.perf_counter()
    process_cases(input_file, output_file)
    print('--> Total time: %.2f' % (time.perf_counter() - start_time))