import fileinput
import math


def get_best_stall(stalls_state):
    max_amount_of_falses = 0
    index_of_max_amount = 0
    current_amount_of_falses = 0
    
    for stall_index, stall_state in enumerate(stalls_state):
        if stall_state:
            if current_amount_of_falses > max_amount_of_falses:
                index_of_max_amount = stall_index - current_amount_of_falses
                max_amount_of_falses = current_amount_of_falses                
                
            current_amount_of_falses = 0
        else:
            current_amount_of_falses += 1

    min = max_amount_of_falses / 2
    max = min
    if max_amount_of_falses % 2 == 0:
        min -= 1

    return index_of_max_amount + int(min), max, min


def last_person_distance(amount_of_user_stalls, amount_of_users):
    all_stalls = [True] + amount_of_user_stalls * [False] + [True]

    for i in xrange(amount_of_users):
        stall_index, max, min = get_best_stall(all_stalls)
        all_stalls[stall_index] = True
        
    return int(max), int(min)


def main():
    input = [line.strip() for line in fileinput.input()]
    case_count = int(input[0])
    
    for i in xrange(1, case_count + 1):
        n, k = input[i].split()
        n = long(n)
        k = long(k)
        max_distance, min_distance = last_person_distance(n, k)
        print "Case #{}: {} {}".format(i, max_distance, min_distance)


if __name__ == "__main__":
    main()
