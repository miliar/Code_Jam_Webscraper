from collections import defaultdict

def solve(inp):
    tmp_dict = defaultdict(int)
    n, k = map(int, inp.split())
    if n==k:
        return '0 0'
    tmp_dict[n] = 1
    while k > 0:
        current_key = max(tmp_dict.keys())
        current_stalls = tmp_dict[current_key]
        if current_stalls >= k:
            ans = current_key - 1

            if ans % 2 == 0:
                return '{} {}'.format(ans // 2, ans//2)
            else:
                return '{} {}'.format((ans-1) // 2 + 1, (ans-1) // 2)
        tmp_dict.pop(current_key)
        current_key -= 1
        k -= current_stalls
        if current_key % 2 == 0:
            tmp_dict[current_key//2] += 2 * current_stalls
        else:
            tmp_dict[(current_key - 1) // 2] += current_stalls
            tmp_dict[(current_key - 1) // 2 + 1] += current_stalls


input = open('in.txt', 'r')
output = open('out.txt', 'w')
t = int(input.readline())
for test_case in range(t):
    output.write('Case #{}: {}\n'.format(test_case + 1, solve(input.readline())))