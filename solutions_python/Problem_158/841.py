def calculate_time(starting_people, plates):
    minutes = 0
    found = False
    min_ = 0
    for number_pan in plates:
        if number_pan > 6:
            n = number_pan / 4
            if number_pan % 4 == 0:
                n -= 1
            minutes += (n + 4)
            found = True
        continue
        min_ = number_pan
    if min_ == 4:
        return 3
    if min_ > 4:
        return 4
    return min_


def process(case_no):
    starting_people = int(raw_input())
    plates = map(int, raw_input().split())
    result = calculate_time(starting_people, plates)
    print('Case #{}: {}'.format(case_no, result))

if __name__ == '__main__':
    t = int(raw_input())
    for i in range(t):
        process(i + 1)
