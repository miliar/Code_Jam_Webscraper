# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
def formatted(answer, curr_case):
    return 'Case #{}: {}'.format(curr_case, str(int(answer)))

def answer(line):
    line_list = [int(d) for d in str(line)]
    line_len = len(line_list)
    reversed_list = list(reversed(line_list))
    ##print(line_list)
    ##print(reversed_list)
    num_nines = 0
    for key in range(len(line_list) - 1):
        if reversed_list[key] < reversed_list[key+1]:
            num_nines = key+1
            reversed_list[key + 1] -= 1

    if num_nines != 0:
        final_list = line_list[0:line_len - num_nines -1]
        final_list.append(str(int(line_list[line_len - num_nines -1])-1))
        final_list.extend(['9'] * num_nines)
        final_list = [str(d) for d in final_list]
        return ''.join(final_list)
    else:
        return line

t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    line = input()
    print(formatted(answer(line), i))

'''
for i in range(1, 10**18 + 1):
    print(formatted(answer(str(i)), i))
'''
