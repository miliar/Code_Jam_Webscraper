from itertools import combinations, chain

f = open('C-test.in')
line_count = int(f.readline())

cases = []

for i in range(line_count):
    input_parts = list(int(part) for part in f.readline().strip().split(' '))

    contestants = int(input_parts[0])

    assert(len(input_parts) == contestants + 1)

    cases.append([int(p) for p in input_parts[1:]])

print(cases)

def solve(numbers):
    sum_dict = {}

    for subset in chain(*(combinations(numbers, i) for i in range(1,len(numbers)))):
        #print(subset)
        s = sum(subset)
        #print(s)
        if s in sum_dict:
            #print('success!')
            #print(subset)
            #print(sum_dict[s])
            return (subset, sum_dict[s])

        sum_dict[s] = subset
    return None


out_lines = []
out_file = open('C-small.out', 'w')

for i, case in enumerate(cases, 1):
    solution = solve(case)

    print(solution)

    out_file.write('Case #{0}:\n'.format(i))

    if solution == None:
        out_file.write('Impossible')
    else:
        out_file.write('{0}\n'.format(''.join(str(s)+' ' for s in solution[0]).strip()))
        out_file.write('{0}\n'.format(''.join(str(s)+' ' for s in solution[1]).strip()))
        print('{0}\n'.format(''.join(str(s)+' ' for s in solution[0]).strip()))
        print('{0}\n'.format(''.join(str(s)+' ' for s in solution[1]).strip()))


out_file.close()
print(out_lines)

