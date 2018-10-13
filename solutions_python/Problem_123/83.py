
def read_input(filename):
    data = []
    with file(filename, 'rt') as f:
        for line in f:
            data.append(line)
        
    case_num = int(data[0].strip())
	
    boards = []
    curr_line = 1
    for _ in xrange(case_num):
        curr_data = data[curr_line]
        first_size, vec_size = curr_data.split()
        first_size = int(first_size)
        vec_size = int(vec_size)
        
        curr_line += 1
        vec_str = data[curr_line]
        vec = [int(i) for i in vec_str.split()]
        vec.sort()
        curr_line += 1

        boards.append((first_size, vec))

    print boards
    return boards

def get_min(size, vec, changes):
    if not vec:
        return changes
       
    print size, vec
    if size > vec[0]:
        return get_min(size + vec[0], vec[1:], changes)
    else:
        remove_all = len(vec[0:]) + changes
        
        if size > 1:
            try_add_changes = get_min(size * 2 - 1, vec, changes + 1)
        else:
            try_add_changes = remove_all
        
        return min(remove_all, try_add_changes)

def get_num(boards):
    res = []
    for board in boards:
        curr_size, vec = board
        res.append(get_min(curr_size, vec, 0))
        
    print res
    return res

def create_output(res):
    with file('output1.txt', 'wt') as f:
        for (i, line) in enumerate(res):
            print >> f, 'Case #%d: %d' % (i + 1, line) 
            
def main():
    import sys
    data = read_input(sys.argv[1])
    res = get_num(data)
    create_output(res)

if __name__ == "__main__":
    main()