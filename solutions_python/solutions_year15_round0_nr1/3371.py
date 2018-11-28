import sys

def solve(a, b):
    max_shy = int(a)
    sum = 0
    k = 0
    answer = 0
    for s in b:
        peeps = int(s)
        if not peeps:
            # if we don't have peeps, then we don't need to add peeps
            k += 1
            continue
        # if we don't have enough peeps, add the min amount necessary
        curr_peeps_needed = 0 if sum >= k else k - sum
        # update our sum of peeps before moving on to next group
        sum += peeps
        sum += curr_peeps_needed
        answer += curr_peeps_needed
        # if our sum is greater than the shyest person, we're done already
        if sum >= max_shy:
            break
        # TODO: if no more 0s, then we're done
        k += 1
    return answer

def write_answer(num, a):
    print "Case #{}: {}".format(num, a)

if __name__ == "__main__":
    line_num = 0
    for line in sys.stdin:
        if line_num == 0:
            num_probs = int(line)
        else:
            l = line.split(" ")
            a = solve(l[0], l[1].strip())
            write_answer(line_num, a)
        line_num += 1
