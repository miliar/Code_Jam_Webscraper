def read_input(filename):
    data = []
    with file(filename, 'rt') as f:
        for line in f:
            data.append(line)
        
    case_num = int(data[0].strip())
    ind = 1
    all_lines = []
    for _ in xrange(case_num):
        case_lines = int(data[ind].strip())
        ind += 1
        lines = data[ind:ind + case_lines]
        curr_case = []
        for line in lines:
            line_data = line.split()
            
            new_line_data = []
            for l in line_data:
                new_line_data.append(int(l))
            curr_case.append(new_line_data)
        all_lines.append(curr_case)
        ind += case_lines
            
    return all_lines    
                
def calc_games(data):
    results = []
    for game in data:
        print 'Game:', game
        curr_stars = 0
        finished_levels = [0] * len(game)
        can_finish = True
        counter = 0
        
        while (any(x != 2 for x in finished_levels)) and can_finish:
            counter += 1
            do_level = -1
            level_finished = False
            level_max = 0
            max_finished = 0
            
            # Finding best thing to do num
            for (i, level) in enumerate(game):
                if finished_levels[i] != 2:
                    if level[1] <= curr_stars and finished_levels[i] >= max_finished:
                        do_level = i
                        level_finished = True
                        max_finished = finished_levels[i]
                    elif level[0] <= curr_stars and level[1] > level_max and finished_levels[i] < 1 and not level_finished:
                        do_level = i
                        level_max = level[1]
                   
            if do_level == -1:
                can_finish = False
            else:
                if level_finished:
                    if finished_levels[do_level] == 0:
                        curr_stars += 2
                    else:
                        curr_stars += 1
                    finished_levels[do_level] = 2
                else:
                    finished_levels[do_level] = 1
                    curr_stars += 1
                    
            print do_level, curr_stars
                    
        if not can_finish:
            results.append('Too Bad')
        else:   
            results.append(str(counter))
            
    return results
          
def create_output(nums):
    with file('outputa.txt', 'wt') as f:
        for (i, num) in enumerate(nums):
            print >> f, 'Case #%d: %s' % (i + 1, num) 
            
def main():
    import sys
    data = read_input(sys.argv[1])
    bests = calc_games(data)
    create_output(bests)

if __name__ == "__main__":
    main()