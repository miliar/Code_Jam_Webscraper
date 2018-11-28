# -------------------
# about


# solution to code jam 2012 - qualification B
# usage: python -O dancing_with_the_Googlers.py
# Python 2.7.2
# 2012-04-14


# -------------------
# computing


# given a satisfying result of points and the total points of a dancer, return whether the best result can be at least satisfying, without/with the help of surprising gradings
def can_be_great(standard, total):
    surprising_margin = 2
    num_referees = 3
    truly_great, surprisingly_great = False, False
    if standard == 0:
        truly_great, surprisingly_great = True, True
        return truly_great, surprisingly_great
    
    if 0 < standard + (standard - surprising_margin + 1) * (num_referees - 1) <= total:
        truly_great, surprisingly_great = True, True
        return truly_great, surprisingly_great
    elif 0 < standard + (standard - surprising_margin) *(num_referees - 1) <= total:
        truly_great, surprisingly_great = False, True
        return truly_great, surprisingly_great
    return truly_great, surprisingly_great


def count_potential_great(standard, num_surprising, list_of_total_scores):
    if len(list_of_total_scores) == 0: # no dancers at all
        return 0
    
    truly_count = 0
    surprisingly_count = 0
    for total in list_of_total_scores:
        truly_great, surprisingly_great = can_be_great(standard, total)
        if truly_great:
            truly_count += 1
        elif surprisingly_great:
            surprisingly_count += 1

     # truly_great can cover if surprisingly_great is short
     # surprisingly_great can be disqualified should surprising quota exceed
    return truly_count + min(num_surprising, surprisingly_count)


def solve(f_name_in, f_name_out):
    f_in = open(f_name_in, 'r')
    num_tests = int(f_in.readline().split()[0])
    f_out = open(f_name_out, 'w')
    for i in range(0,num_tests):
        case_num = i+1
        line_data = [int(x) for x in f_in.readline().split()]
        num_googlers = line_data[0]
        num_surprising = line_data[1]
        standard = line_data[2]
        list_of_total_scores = line_data[3:]
        assert len(list_of_total_scores) == num_googlers
        count = count_potential_great(standard, num_surprising, list_of_total_scores)
        result = 'Case #%d: %d\n' %(case_num, count)
        f_out.write(result)
    f_in.close()
    f_out.close()


# -------------------
# solving
solve('B-large.in', 'B-large.out')
