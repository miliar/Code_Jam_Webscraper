import sys

def run_test(case_number, generator):
    shyness = [int(x) for x in next(generator).split()[1]]
    count = 0
    added = 0
    for i in range(len(shyness)):
        if i > count:
            added += i - count
            count = i
        count += shyness[i]
    print('Case #%d: %d' % (case_number, added))

def main():
    generator = get_file()
    number_of_tests = int(next(generator))
    for test in range(1, number_of_tests + 1):
        run_test(test, generator)

def get_file():
    for line in sys.stdin:
        yield line
        
if __name__ == '__main__':
    main()