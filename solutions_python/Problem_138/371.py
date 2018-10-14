
import time


input_file = 'D-large.in'
#input_file = 'D-small-attempt0.in'
#input_file = 'D.txt'

output_file = input_file + '.txt'

DEBUG = True
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

def take_smallest_bigger_than(blocks, weight):
    r_i, r_b = None, 2.0
    for i, b in enumerate(blocks):
        if b is not None and b > weight and b < r_b:
            r_i, r_b = i, b
    if r_i is not None:
        blocks[r_i] = None
        return r_b
    return None

def get_max(blocks):
    r_i, r_b = None, -1.0
    for i, b in enumerate(blocks):
        if b is not None and b > r_b:
            r_i, r_b = i, b
    assert r_i is not None
    return (r_i, r_b)

def get_min(blocks):
    r_i, r_b = None, 2.0
    for i, b in enumerate(blocks):
        if b is not None and b < r_b:
            r_i, r_b = i, b
    assert r_i is not None
    return (r_i, r_b)

def play_fair_k(blocks_k, weight):
    assert any(blocks_k)
    if take_smallest_bigger_than(blocks_k, weight):
        return True
    else:
        take_smallest_bigger_than(blocks_k, -1)
        return False
    
def play_fair_n(blocks_n, blocks_k):
    assert any(blocks_n)
    i, weight = get_max(blocks_n)
    blocks_n[i] = None
    return not play_fair_k(blocks_k, weight)    

delta = 0.0000001
def play_deceit_n(blocks_n, blocks_k):
    assert any(blocks_n)
    weight = take_smallest_bigger_than(blocks_n, get_min(blocks_k)[1])
    if weight is not None:
        return not play_fair_k(blocks_k, get_max(blocks_k)[1] + delta)
    else:
        weight = take_smallest_bigger_than(blocks_n, -1)
        return not play_fair_k(blocks_k, get_max(blocks_k)[1] - delta)

def solve_case(file):
    rounds = int(file.readline())
    blocks_n = list(map(float, file.readline().strip().split()))
    blocks_k = list(map(float, file.readline().strip().split()))
    
    blocks_fair_n = list(blocks_n)
    blocks_fair_k = list(blocks_k)
    score_fair_n = 0
    for r in range(rounds):
        if play_fair_n(blocks_fair_n, blocks_fair_k):
            score_fair_n += 1

    blocks_deceit_n = list(blocks_n)
    blocks_deceit_k = list(blocks_k)
    score_deceit_n = 0
    for r in range(rounds):
        if play_deceit_n(blocks_deceit_n, blocks_deceit_k):
            score_deceit_n += 1
            
    return '%d %d' % (score_deceit_n, score_fair_n)
    
#----------------------------------------------------------------------------------------------------------------------            
    
if __name__ == "__main__":
    start_time = time.perf_counter()
    process_cases(input_file, output_file)
    print('--> Total time: %.2f' % (time.perf_counter() - start_time))
