import math
def bathroom_stalls(num_stalls,num_people):
    num_people_prev = num_people - 1
    open_stalls_prev = num_stalls - num_people_prev
    partitions_prev = num_people_prev + 1
    bisections_prev = math.floor(math.log(partitions_prev,2))
    bisecting_people_prev = 2**bisections_prev-1
    remaining_people_prev = num_people_prev - bisecting_people_prev
    largest_open_prev = math.ceil(open_stalls_prev / (2**bisections_prev))

    smallest_open = math.floor((largest_open_prev - 1) / 2)
    largest_open = math.ceil((largest_open_prev - 1 ) / 2)
    return(largest_open, smallest_open)

def solve_file(file_path):
    f = open(file_path)
    solution = open('stalls_results.txt','w')
    # skip first line and read remaining lines
    case_number = 1
    for line in f.readlines()[1:]:
        if line[0] != '#':
            result = bathroom_stalls(int(line.split()[0]),int(line.split()[1]))
            print('Case #{}: {} {}'.format(case_number,*result),file=solution)
            case_number += 1

solve_file('C-small-2-attempt0.in')
