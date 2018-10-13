import math

def read_input(filename):
    data = []
    with file(filename, 'rt') as f:
        for line in f:
            data.append(line)
        
    case_num = int(data[0].strip())
	
    cases = []
    curr_line = 1
    for _ in xrange(case_num):
        curr_data = data[curr_line]
        n, p = curr_data.split(' ')
        n = int(n)
        p = int(p)
        cases.append((n, p))
        curr_line += 1

    return cases

def get_min_to_win(n, p):
    teams = 2**n
    min_to_win = teams - p

    curr_zeros = [0] * teams
    big_count = 2
    little_count = 0
    ind = 1
    zeros = 1
    while True:
        curr_zeros[ind] = zeros
        ind += 1
        if ind == teams:
            break
            
        little_count += 1
        if little_count == big_count:
            big_count *= 2
            little_count = 0
            zeros += 1
   
    curr_zeros = [2 ** (n - zeros) - 1 for zeros in curr_zeros]        
    
    for i in xrange(0, teams):
       if curr_zeros[i] >= min_to_win:
          curr_win = i
       else:
          break
          
    return curr_win
    
def get_max_can_win(n, p):
    teams = 2**n
    min_to_win = teams - p
    
    curr_zeros = [0] * teams
    big_count = teams / 2
    little_count = 0
    ind = 1
    zeros = 1
    while True:
        curr_zeros[ind] = zeros
        ind += 1
        if ind == teams:
            break
            
        little_count += 1
        if little_count == big_count:
            big_count /= 2
            little_count = 0
            zeros += 1
   
    curr_zeros = [2 ** n - 2 ** zeros for zeros in curr_zeros]        
    
    for i in xrange(0, teams):
       if curr_zeros[i] >= min_to_win:
          curr_win = i
       else:
          break
          
    return curr_win

def get_num(cases):
    res = []
    for case in cases:
        n, p = case
        min_win = get_min_to_win(n, p)
        max_can = get_max_can_win(n, p)
        res.append((min_win, max_can))
        
    print res
    return res

def create_output(res):
    with file('output1.txt', 'wt') as f:
        for (i, line) in enumerate(res):
            print >> f, 'Case #%d: %d %d' % (i + 1, line[0], line[1]) 
            
def main():
    import sys
    data = read_input(sys.argv[1])
    res = get_num(data)
    create_output(res)

if __name__ == "__main__":
    main()