import sys

def calculate(smax, persons):
    invited_friends = 0
    current_shyness_level = 0
    standing_persons = 0
    for p in persons:
        need_friends = (abs(current_shyness_level - standing_persons) + (current_shyness_level - standing_persons)) / 2
        invited_friends += need_friends
        standing_persons += need_friends
        current_shyness_level += 1
        standing_persons += p
    return invited_friends
    
def parse_input_line(line):
    smax, persons_string = line.split(' ')
    persons = [int(x) for x in persons_string]
    return (smax, persons)

def read_data(file_name):
    test_cases = list()
    with open(file_name) as fl:
        t = int(fl.readline())
        for i in range(t):
            (smax, persons) = parse_input_line(fl.readline().strip())
            test_cases.append((smax, persons))
    return test_cases

def main():
    file_name = sys.argv[1]
    data = read_data(file_name)
    case = 1
    with open('output.txt', 'w') as fl:
        for (smax, persons) in data:
            result = calculate(smax, persons)
            fl.write('Case #{0}: {1}\n'.format(case, result))
            case += 1

if __name__ == '__main__':
    main()