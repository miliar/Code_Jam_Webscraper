

def load_data(filename):

    with open(filename) as file_handle:
        content = file_handle.read().splitlines()

    num_cases = int(content[0])
    
    retval = []
    for idx in range(1, num_cases+1):
        sample = content[idx]
        pancakes, k = sample.split(' ', 2)
        retval.append((pancakes, int(k)))

    return retval

def flip(pancakes, k, posn):
    
    pancake_list = list(pancakes)
    for idx in range(posn, posn + k):
        if pancake_list[idx] == '+':
            pancake_list[idx] = '-'
        else:
            pancake_list[idx] = '+'
            
    return "".join(pancake_list)
    

def get_num_flips(pancakes, k):
    
    flip_count = 0
    
    # start at the leftmost minus
    for idx in range(0, len(pancakes) - k + 1):
        if pancakes[idx] == '-':
            # flip and move to the next minus
            pancakes = flip(pancakes, k, idx)
            flip_count += 1

    if pancakes.find('-') > -1:
        flip_count = -1
        
    return flip_count
    
def main():
    
    input_file = 'A-small-attempt0.in'
    pancake_list = load_data(input_file)
    idx = 1;
    
    for pancake_tuple in pancake_list:
        #print("{}: {}".format(pancake_tuple[1], pancake_tuple[0]))
        flips = get_num_flips(pancake_tuple[0], pancake_tuple[1])
        if flips < 0:
            flips = 'IMPOSSIBLE'
        print("Case #{}: {}".format(idx, flips))
        idx += 1

if __name__ == '__main__':
    main()
