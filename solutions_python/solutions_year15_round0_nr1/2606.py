import sys

cases = []

def load_cases(filename):
    f = open(filename,'rU')
    number_of_cases = int(f.readline())

    cases = []

    for i in range(0,number_of_cases):
        case = f.readline().split()
        cases.append(case)

    return cases


def solve_case(case):
    max_shyness = int(case[0])
    audience = case[1]
    people_seated = 0
    to_be_invited = 0

    for shyness_level in range(0,max_shyness+1):
        number_of_people = int(audience[shyness_level])

        if number_of_people > 0:
            if people_seated >= shyness_level:
                people_seated += number_of_people
            else:
                to_be_invited += shyness_level - people_seated
                people_seated += shyness_level - people_seated + number_of_people

    return str(to_be_invited)

def main():
    args = sys.argv[1:]

    if not args:
        print('no file specified')
        sys.exit(1)

    file = args[0]

    cases = load_cases(file)
    case_number = 0

    for case in cases:
        case_number += 1
        print('Case #' + str(case_number) + ': ' + solve_case(case))


if __name__ == '__main__':
    main()
