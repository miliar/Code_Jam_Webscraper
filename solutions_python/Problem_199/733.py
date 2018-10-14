def solve(inp):
    ans = 0
    pancakes_tmp, k_tmp = inp.split(' ')
    k = int(k_tmp)
    pancakes = [_ for _ in pancakes_tmp]
    cake_index = 0
    while cake_index < len(pancakes):
        if pancakes[cake_index] == '-':
            ans += 1
            for shift_item in range(k):
                if cake_index + shift_item < len(pancakes):
                    if pancakes[cake_index + shift_item] == '-':
                        pancakes[cake_index + shift_item] = '+'
                    else:
                        pancakes[cake_index + shift_item] = '-'
                else:
                    return 'IMPOSSIBLE'
        cake_index += 1
    return ans

input = open('in.txt', 'r')
output = open('out.txt', 'w')
t = int(input.readline())
for test_case in range(t):
    output.write('Case #{}: {}\n'.format(test_case + 1, solve(input.readline())))