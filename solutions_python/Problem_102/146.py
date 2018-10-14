def read_input(filename):
    data = []
    with file(filename, 'rt') as f:
        for line in f:
            data.append(line)
        
    line_num = int(data[0].strip())
    lines = [data[i].strip() for i in xrange(line_num + 1)]
    lines = lines[1:]
    assert len(lines) == line_num
            
    return lines
    
def get_mins(data):
    line_vals = [int(x) for x in data.split()]
    cont_num = line_vals[0]
    scores = line_vals[1:]
    all_add = sum(scores)
    assert len(scores) == cont_num
        
    mins = [0] * cont_num
    have_min = [False] * cont_num
    
    have_all_zeros = False
    while not have_all_zeros:
        have_all_zeros = True
        full_sum = sum(scores)
        max_score = full_sum + all_add
        min_needed = max_score / float(cont_num)
        
        for (i, score) in enumerate(scores):
            if not have_min[i] and score >= min_needed:
                have_min[i] = True
                scores[i] = 0
                have_all_zeros = False
                cont_num -= 1
                
    print full_sum, max_score, min_needed
    
    for i in xrange(len(scores)):
        if not have_min[i]:
            needed_score = min_needed - scores[i]
            if needed_score <= 0:
                mins[i] = 0
                continue
            mins[i] = needed_score * 100 / float(all_add)
        
    return mins
        
def create_output(nums):
    print nums
    with file('outputa.txt', 'wt') as f:
        for (i, num) in enumerate(nums):
            vals = ''
            for j in num:
                vals += '%.6lf ' % (j, )
                
            print >> f, 'Case #%d: %s' % (i + 1, vals) 
            
def main():
    import sys
    data = read_input(sys.argv[1])
    
    mins = []
    for line in data:
        curr_mins = get_mins(line)
        mins.append(curr_mins)
        
    create_output(mins)

if __name__ == "__main__":
    main()