import sys

def combine_step(cp, result_list):
    if (len(result_list) < 2): return result_list

    list_tail = result_list[-2]
    new_item = result_list[-1]

    for ((a,b),c) in cp:
        if ( (list_tail == a and new_item == b) or (list_tail == b and new_item == a) ):
            result_list = result_list[0:-2]
            result_list.append(c)
            return result_list
    return result_list

def clear_step(op, cur_list):
    for (a,b) in op:
        if (a in cur_list and b in cur_list):
            return []
    return cur_list

def solve(cp, op, seq):
    result_list = []
    for item in seq:
        result_list.append(item)                
        
        result_list = combine_step(cp, result_list)
        next_result_list = combine_step(cp, result_list)
        while (next_result_list != result_list):
           result_list = combine_step(cp, result_list)
           next_result_list = combine_step(cp, result_list)

        result_list = clear_step(op, result_list)
    return result_list

f = open(sys.argv[1], "r")
output_name = sys.argv[1] + ".results"
output = open(output_name, "w+")

num_cases = int(f.readline())
case_id = 1
for line in f.readlines():
    combine_pairs = []
    opposed_pairs = []

    tc_raw = line.split(' ')
    num_combine_pairs = int(tc_raw[0])

    for cp in tc_raw[1:num_combine_pairs+1]:
        combine_pairs.append( ((cp[0], cp[1]), cp[2]) )
    
    num_opposed_pairs = int(tc_raw[num_combine_pairs + 1])
    if (num_opposed_pairs > 0):
        for op in tc_raw[num_combine_pairs + 2 : len(tc_raw) - 2]:
            opposed_pairs.append((op[0], op[1]))
            
    sequence = tc_raw[len(tc_raw) - 1]
    solution = solve(combine_pairs, opposed_pairs, sequence.strip())
    str_sol = "Case #%d: [" % (case_id)
    for c in solution:
        str_sol += c + ", "
    if (len(solution) > 0):
        str_sol = str_sol[0:-2]

    str_sol += "]"

    output.write(str_sol + "\n")    
    print str_sol
    
    case_id += 1
    
f.close()
output.close()