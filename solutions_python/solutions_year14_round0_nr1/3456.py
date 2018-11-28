import sys

def find_card(g1, a1, g2, a2):
    potential_cards1 = a1[g1-1]
    potential_cards2 = a2[g2-1]
    variants = potential_cards1 & potential_cards2
    if len(variants) == 0:
        return 'Volunteer cheated!'
    elif len(variants) > 1:
        return 'Bad magician!'
    return variants.pop()

def read_data(file_name):
    test_cases = list()
    with open(file_name) as f:
        t = int(f.readline())
        for i in range(t):
            first_answer = int(f.readline())
            first_arrangement = list()
            for n in range(4):
                first_arrangement.append(set(int(i) for i in f.readline().strip().split(' ')))
            second_answer = int(f.readline())
            second_arrangement = list()
            for n in range(4):
                second_arrangement.append(set(int(i) for i in f.readline().strip().split(' ')))
            test_cases.append((first_answer, first_arrangement, second_answer, second_arrangement))
    return test_cases

def main():
    file_name = sys.argv[1]
    data = read_data(file_name)
    case = 1
    with open('output.txt', 'w') as f:
        for (g1, a1, g2, a2) in data:
            result = find_card(g1, a1, g2, a2)
            f.write('Case #{0}: {1}\n'.format(case, result))
            case += 1

if __name__ == '__main__':
    main()