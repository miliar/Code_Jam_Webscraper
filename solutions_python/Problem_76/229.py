def binary_conversion(n):
    # assume n (C_i) <= 10**6
    # 2**19 < 10**6 < 2**20
    result = []
    running_value = n
    power_of_2 = 2**20
    while power_of_2 > 1:
        power_of_2 = power_of_2/2
        digit = running_value/power_of_2
        result.append(digit)
        running_value -= digit*power_of_2
    return result

def splits_helper(n):
    if n == 1:
        return [[0], [1]]

    return [[0] + perm for perm in splits_helper(n - 1)] + \
           [[1] + perm for perm in splits_helper(n - 1)]

# def splits(n):
#     index_sets = splits_helper(n)

#     result = []
#     for index_set in index_sets:
#         result.append([index for index in range(n) if index_set[index]])

#     return result

def splits(n):
    result = [[0], [1]]
    max_ones = n/2 # integer division intended
    for length in range(2, n + 1):
        new_result = []
        for val in result:
            new_result.append(val + [0])
            if sum(val) < max_ones:
                new_result.append(val + [1])
        result = new_result

    complement_pairs = []
    for val in result:
        complement = [1 - digit for digit in val]
        if not ((val, complement) in complement_pairs
                or (complement, val) in complement_pairs):
            complement_pairs.append((val, complement))

    index_pairs = []
    for first, second in complement_pairs:
        first_indices = [index for index in range(n) if first[index]]
        second_indices = [index for index in range(n) if second[index]]
        index_pairs.append((first_indices, second_indices))

    return index_pairs

# Sum of a group can never increase number of binary
# digits. Since no carrying occurs, the summing
# is independent in each digit. Since 0's don't effect
# the outcome, only the ones in sequence will have
# an effect.

# Let S(P, d) be the d-th digit of the sum of a pile P
# clear S(P, d) = 0 if number of 1's in location d in P is even, else 1

# Hence if we have two piles P, Q, we'll need
# S(P, d) = S(Q, d) for all d

# But if there are an odd number of 1's in any of the locations (in
# combined P + Q) we can't do the sum

# Starting from the lead digit, we can recursively generate candidate
# piles and

#101
#100
#011
#010
#001

def patrick_sum(binary_pile):
    result = [0]*20
    for index in range(20):
        result[index] = sum([binary[index] for binary in binary_pile]) % 2
    return result

def is_possible(binary_pile):
    return sum(patrick_sum(binary_pile)) == 0

def solution(pile, splits_hash):
    binary_pile = [binary_conversion(val) for val in pile]
    if not is_possible(binary_pile):
        return "NO"

    n = len(pile)
    if n in splits_hash:
        possible_splits = splits_hash[n]
    else:
        possible_splits = splits(n)
        splits_hash[n] = possible_splits

    curr_max = -1
    for first, second in possible_splits:
        first_pile = [pile[index] for index in first]
        second_pile = [pile[index] for index in second]

        if first_pile and second_pile:
            first_pile_binary = [binary_conversion(val)
                                 for val in first_pile]
            second_pile_binary = [binary_conversion(val)
                                  for val in second_pile]
            if (patrick_sum(first_pile_binary) ==
                patrick_sum(second_pile_binary)):
                pat_val = max(sum(first_pile), sum(second_pile))
                curr_max = max(pat_val, curr_max)

    if curr_max == -1:
        raise Exception("No solution found")
    return curr_max

def parse_cases(data):
    lines = [row for row in data.split('\n') if row]
    cases = int(lines[0])
    result = []
    for problem in range(1, cases + 1):
        num_candies = int(lines[2*problem - 1])
        candies = [int(val) for val in lines[2*problem].split()]
        if len(candies) != num_candies:
            raise Exception("Bad data")
        result.append(candies)
    return cases, result

with open('C-small-attempt1.in.in.in', 'r') as fh:
    cases, data = parse_cases(fh.read())

all_splits = {}
result = ''
for problem in range(1, cases + 1):
    solution_val = solution(data[problem - 1], all_splits)
    result += 'Case #%s: %s\n' % (problem, solution_val)
    print 'Case #%s: %s' % (problem, solution_val)

result = result.strip() # trailing newline

with open('C-small-output.out', 'w') as fh:
    fh.write(result)
