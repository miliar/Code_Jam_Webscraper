import math

def read_input(filename):
    data = []
    with file(filename, 'rt') as f:
        for line in f:
            data.append(line)
        
    line_num = int(data[0].strip())
	
    lines = []
    for i in xrange(line_num):
        lines.append([int(x) for x in data[i + 1].split()])

    print lines
    return lines

def is_fns(num):
    str_num = str(num)
    if str_num != str_num[::-1]:
        return False

    sq = math.sqrt(num)
    if sq != int(sq):
        return False
        
    str_sq = str(int(sq))
    if str_sq != str_sq[::-1]:
        return False
        
    return True
    
def calc_fair_and_square(start, end):
    vec = [False for _ in xrange(end + 1)]
    
    for i in xrange(start, end + 1):
        vec[i] = is_fns(i)
        
    return vec

def get_res(data):
    # First of all, getting real endpoints
    start = min([x[0] for x in data])
    end = max([x[1] for x in data])
    
    # Calculating for entire scope
    is_fair_and_square = calc_fair_and_square(start, end)
        
    # For every line, counting how many FNSs are in it
    res = [is_fair_and_square[line[0]:line[1]+1].count(True) for line in data]
    
    print res
    return res

def create_output(res):
    with file('output1.txt', 'wt') as f:
        for (i, line) in enumerate(res):
            print >> f, 'Case #%d: %d' % (i + 1, line) 
            
def main():
    import sys
    data = read_input(sys.argv[1])
    res = get_res(data)
    create_output(res)

if __name__ == "__main__":
    main()