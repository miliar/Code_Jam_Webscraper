import sys
inputs = sys.stdin

def solution(inputs):
    pancake_counts = [int(x) for x in inputs]
    accum_special_mins = 0
    def distribute_pancakes(pancake_counts, reduce_factor=2):
        pancake_counts.sort()
        btlnk = pancake_counts[-1]
        btlnk_count = pancake_counts.count(btlnk)
        rest = pancake_counts[:-btlnk_count]
        split_count = reduce_factor - 1
        sub_amount = btlnk/reduce_factor
        splited_btlnk = btlnk - split_count*sub_amount
        mins_for_split = btlnk_count * split_count
        updated_pancake_counts = rest + [splited_btlnk]*btlnk_count + [sub_amount]*reduce_factor*btlnk_count
        return updated_pancake_counts, mins_for_split

    def get_total_time(special_move_mins, pancake_counts, reduce_factor=2):
        btlnk = max(pancake_counts)
        updated_pancake_counts, mins_for_split = distribute_pancakes(pancake_counts)
        special_move_mins += mins_for_split
        new_btlnk = max(updated_pancake_counts)
        updated_time_elapsed = special_move_mins + new_btlnk
        if new_btlnk in [1, 2]:
            return updated_time_elapsed
        elif btlnk == 9:
            updated_pancake_counts_3, mins_for_split_3 = distribute_pancakes(pancake_counts, reduce_factor=3)
            special_move_mins_3 = special_move_mins - mins_for_split + mins_for_split_3
            new_btlnk_3 = max(updated_pancake_counts_3)
            updated_time_elapsed_3 = special_move_mins_3 + new_btlnk_3
            return min(min(updated_time_elapsed, get_total_time(special_move_mins, updated_pancake_counts)) , min(updated_time_elapsed_3, get_total_time(special_move_mins_3, updated_pancake_counts_3)))
        else:
            return min(updated_time_elapsed, get_total_time(special_move_mins, updated_pancake_counts))
    return min(max(pancake_counts), get_total_time(accum_special_mins, pancake_counts))

orig_stdout = sys.stdout
output = file('output.out', 'w')
sys.stdout = output

case_count = int(inputs.readline())
for idx in xrange(1, case_count + 1):
    plates_count = inputs.readline()
    pancake_counts = inputs.readline().split()
    result = solution(pancake_counts)
    print "Case #{}: {}".format(idx, result)

sys.stdout = orig_stdout
output.close()
