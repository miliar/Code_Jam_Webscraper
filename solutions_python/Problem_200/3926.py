def calculate_answer(n):
    digits = [int(i) for i in str(n)]
    prev_index = -1
    all_9_index = -1
    prev_loop_index = -1
    loop_index = len(digits)-1
    for i in xrange(loop_index):
        if digits[i] == digits[i+1] and prev_index == -1:
            prev_index = i
        else:
            if digits[i] > digits[i+1]:
                change_index = i
                if prev_index != -1:
                    change_index = min(prev_index, i)
                if digits[change_index] != 0:
                    digits[change_index] -= 1
                else:
                    digits[change_index] = 9
                all_9_index = change_index + 1
                break

    if all_9_index != -1:
        for i in xrange(all_9_index, len(digits)):
            digits[i] = 9

    return int(''.join(map(str,digits)))

in_f = 'B-small.in'
out_f = 'B-small-out.in'
with open(in_f, 'r') as in_file, open(out_f, 'w') as out_file:
    test_cases = int(in_file.readline().strip())
    for t in xrange(1, test_cases + 1):
        num = int(in_file.readline())
        answer = calculate_answer(num)
        out_file.write('Case #' + str(t) + ': ' + str(answer) + '\n')
