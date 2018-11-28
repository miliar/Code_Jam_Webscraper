import itertools

# return binary numbers with up to j 1s
def binary_list_upto(num_digits, j):
    binary_list = []
    for k in range(1, j + 1):
        binary_list.extend([2 ** (num_digits - 1) + sum([2 ** a for a in comb])
                            for comb in list(itertools.combinations(range(0, num_digits - 1), k - 1))])
    return binary_list

# n is the smaller palindrome, n_sq is the larger palindrome
list_fair_and_square = []
for num_digits_n in range(1, 52):
    num_digits_m = (num_digits_n + 1) / 2
    if num_digits_n == 1:
        m_range = range(1, 4)
    else:
        m_range = [int(bin(a)[2:]) for a in binary_list_upto(num_digits_m, 5)]
        m_range.append(2 * 10 ** (num_digits_m - 1))
        if num_digits_n % 2 == 1:
            m_range.extend([int(bin(a)[2:] + '2') for a in binary_list_upto(num_digits_m - 1, 2)])
            m_range.append(2 * 10 ** (num_digits_m - 1) + 1)
    for m in m_range:
        if num_digits_n % 2 == 0:
            n = int(str(m) + str(m)[::-1])
        else:
            n = int(str(m) + str(m)[-2::-1])
        n_sq = n * n
        if str(n_sq) == str(n_sq)[::-1]:
            list_fair_and_square.append(n_sq)

f_in = open('C-large-2.in', 'r')
f_out = open('C-large-2.out', 'w')

num_cases = int(f_in.readline().strip())

for idx_case in range(num_cases):
    A_B_list = f_in.readline().strip().split()
    A = int(A_B_list[0])
    B = int(A_B_list[1])
    
    num_fair_and_square = len([num for num in list_fair_and_square if num >= A and num <= B])
    
    f_out.write('Case #{}: {}\n'.format(idx_case+1, num_fair_and_square))

f_in.close()
f_out.close()