import sys


def solve(max_shyness, audience):
    people_needed = 0
    cumulative = [0] * (max_shyness + 1)
    cumulative[0] = audience[0]
    for i in range(1, max_shyness + 1):
        diff = i - cumulative[i - 1]
        cumulative[i] = cumulative[i - 1] + audience[i]
        if diff > 0:
            people_needed += diff
            cumulative[i] += diff

    return people_needed


filename = sys.argv[1]

with open(filename) as f:
    content = f.readlines()

test_cases = content[0]
with open('output', 'w') as output_file:
    for i in range(1, int(test_cases) + 1):
        split = content[i].split(' ')
        output_file.write('Case #{0}: {1}\n'.format(i, solve(int(split[0]), map(lambda x: int(x), list(split[1][:-1])))))


