def process_test_case(idx, test_line):
    test_sep = test_line.split(' ')
    smax = int(test_sep[0])
    values = test_sep[1]
    additional = 0
    while not standing_ovation(values, additional):
        additional += 1
    print 'Case #%i: %i' % (idx, additional)

def standing_ovation(audience, additional=0):
    nb_stand = int(audience[0]) + additional
    for idx in range(1, len(audience)):
        curr_shyness = int(audience[idx])
        if nb_stand < idx:
            return False
        nb_stand += curr_shyness
    return True

def main():
    nb_test_cases = int(raw_input())
    for idx in range(nb_test_cases):
        test_case = raw_input()
        process_test_case(idx+1, test_case)

if __name__ == "__main__":
    main()
