from copy import deepcopy

MAX = 2000

def read_input(filename):
    data = []
    with file(filename, 'rt') as f:
        for line in f:
            data.append(line)
        
    case_num = int(data[0].strip())
	
    lines = []
    for i in xrange(case_num):
        lines.append([int(i) for i in data[i + 1].split()])

    print lines
    return lines

def get_line_stat(plane, dims, x, y, perc, choice):
    mid = MAX / 2
    x += mid
    
    if dims == 0:
        return 0
    
    # For every diamond falling
    for i in xrange(dims):
        curr_fall = MAX / 2
        falling = True
        
        while falling:
            if plane[curr_fall] > plane[curr_fall - 1] and plane[curr_fall] > plane[curr_fall + 1]:
                # Complicated
                if choice == 0:
                    left_plane = deepcopy(plane)
                    right_plane = deepcopy(plane)
                    return get_line_stat(left_plane, dims - i, x - mid, y, perc * 0.5, 1) + get_line_stat(right_plane, dims - i, x - mid, y, perc * 0.5, 2)
                elif choice == 1:
                    curr_fall -= 1
                elif choice == 2:
                    curr_fall += 1
                choice = 0
            else:
                if plane[curr_fall] == -1:
                    plane[curr_fall - 1] = 0
                    plane[curr_fall] = 1
                    plane[curr_fall + 1] = 0
                    falling = False
                elif plane[curr_fall] > plane[curr_fall + 1]:
                    curr_fall += 1
                elif plane[curr_fall] > plane[curr_fall - 1]:
                    curr_fall -= 1
                else:
                    # Stuck
                    plane[curr_fall] += 2
                    falling = False
                
        if plane[x] >= y:
            return perc
        
    return 0

def get_stat(data):
    res = []
    for i, line in enumerate(data):
        print i
        plane = [-1] * MAX
        dims, x, y = line
        
        if x > dims * 2 or x < -dims * 2:
            res.append(0)
        else:
            res.append(get_line_stat(plane, dims, x, y, 1.0, 0))
       
    print res
    return res

def create_output(res):
    with file('output1.txt', 'wt') as f:
        for (i, line) in enumerate(res):
            print >> f, 'Case #%d: %lf' % (i + 1, line) 
            
def main():
    import sys
    data = read_input(sys.argv[1])
    res = get_stat(data)
    create_output(res)

if __name__ == "__main__":
    main()