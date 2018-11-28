# -------------------
# about


# solution to code jam 2012 - qualification C 
# usage: python -O recycled_numbers.py
# Python 2.7.2
# 2012-04-14


# -------------------
# computation


# given an integer, compute the number of induced distinct recycled pairs in the given range
def count_recycled_pairs(integer, lower, upper):
    assert integer > 0
    assert len(str(lower)) == len(str(upper))
    count = 0
    s_integer = str(integer)
    candidates = []
    for i in range(1,len(s_integer)):      
        s_candidate = s_integer[i:] + s_integer[:i]
        if s_candidate[0] == '0': # leading zero breaks rule
            continue
        else:
            candidate = int(s_candidate)
        if lower <= integer < candidate <= upper:
            assert len(candidates) <= len(s_integer)
            if candidate not in candidates: # sample bug: 1212 > 2121 (two possible paths)
                candidates.append(candidate)
                count += 1
    return count

# given two integers, compute the number of distinct recycled pairs in the range
# time complexity (B-A+1)*len(str(B)-1)
# space complexity (len(str(B)) - 1) ** 2 B
def count_all_recycled_pairs(lower, upper):
    assert 0 < lower < upper
    assert len(str(lower)) == len(str(upper))
    count = 0
    for i in range(lower, upper+1):
        count += count_recycled_pairs(i, lower, upper)
    return count


# solve a task
def solve(f_name_in, f_name_out):
    f_in = open(f_name_in, 'r')
    num_tests = int(f_in.readline().split()[0])
    f_out = open(f_name_out, 'w')
    for i in range(0,num_tests):
        case_num = i+1
        (lower, upper) = [int(x) for x in f_in.readline().split()]
        count = count_all_recycled_pairs(lower, upper)
        result = 'Case #%d: %d\n' %(case_num, count)
        f_out.write(result)
    f_in.close()
    f_out.close()


# -------------------
# solving
solve('C-small-attempt0.in', 'C-small-attempt0.out')
