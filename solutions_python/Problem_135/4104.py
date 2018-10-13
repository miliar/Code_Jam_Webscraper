range(4, 4)

def get_result():
    row = parse_row(int(raw_input()))
    second_row = parse_row(int(raw_input()))

    common_elts = set.intersection(*map(set, [row, second_row]))

    if len(common_elts) == 0:
        return "Volunteer cheated!"
    elif len(common_elts) == 1:
        (elt,) = common_elts
        return str(elt)
    else:
        return "Bad magician!"

def parse_row(chosen_row):
    rows = [raw_input().split() for i in range(chosen_row)]

    # exhaust remaining input
    for i in range(chosen_row, 4):
        raw_input()

    return rows[chosen_row-1]

def run_tests():
    num_tests = int(raw_input())
    tests = []
    for i in range(num_tests):
        print "Case #{0}: {1}".format(i+1, get_result())

if __name__ == '__main__':
    run_tests()