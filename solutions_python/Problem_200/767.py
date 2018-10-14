def solve(n):
    n = n.split()[0]
    n = [_ for _ in n]
    for check_index in range(len(n)-1, -1, -1):
        check_digit = n[check_index]
        for second_index in range(check_index-1, -1, -1):
            second_digit = n[second_index]
            if second_digit > check_digit:
                for correct_index in range(second_index+1, len(n)):
                    n[correct_index] = '9'
                n[second_index] = str(int(n[second_index]) - 1)
                break
    return int(''.join(n))

input = open('in.txt', 'r')
output = open('out.txt', 'w')
t = int(input.readline())
for test_case in range(t):
    output.write('Case #{}: {}\n'.format(test_case + 1, solve(input.readline())))