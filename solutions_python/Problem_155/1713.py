def process_case(case):
    max_s, ppl = case.split()
    if int(max_s) == 0:
        return 0

    prev_count = 0
    num_friends_to_add = 0
    # i is the shyness level
    for i in range(len(ppl)):
        # not enough prev ppl for current group to stand
        if (prev_count < i):
            # make up the difference by adding friends
            num_friends_to_add += (i - prev_count)
            # prev count is now exactly the same as i
            prev_count = i

        # add current group to prev count
        prev_count += int(ppl[i])
    
    return num_friends_to_add

with open('ovation_input.txt', 'r') as f, open('ovation_output.txt', 'w') as g:
    num_tests = int(f.readline().strip())
    for i in range(num_tests):
        num_friends = process_case(f.readline())
        g.write('Case #%s: %s\n' % (i+1, num_friends))
