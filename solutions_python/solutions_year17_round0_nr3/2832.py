import math
import sys


mindata = 0
maxdata = 0

def parse(filename):
    lines = []
    with open(filename, 'r') as f:
        lines = f.readlines()

    test_cases = int(lines[0])
    data = []
    for test in lines[1:test_cases+1]:
        data.append(list(map(int, test.split(' '))))

    return data

def split(data, person_number):
    #  print(person_number, data)
    global mindata, maxdata

    if person_number <= 0 or len(data) == 0:
        return data

    split_pos = math.ceil(len(data)/2) - 1
    person_number -= 1

    if person_number == 0:
        temp_maxdata = max(len(data[:split_pos]), len(data[split_pos+1:]))
        temp_mindata = min(len(data[:split_pos]), len(data[split_pos+1:]))
        #  print(data, data[:split_pos], data[split_pos+1:], temp_maxdata, temp_mindata)
        #  if temp_maxdata >= maxdata and temp_mindata >= mindata:
        mindata = temp_mindata
        maxdata = temp_maxdata

    if data[split_pos] != '0':
        data[split_pos] = '0'
    else:
        print('fail')

    return split(data[:split_pos], int(person_number/2)) + ['0'] + split(data[split_pos+1:], math.ceil(person_number - (int(person_number)/2)))

def reset_min_max():
    global mindata, maxdata

    mindata = - sys.maxsize
    maxdata = - sys.maxsize

def get_best_min_max(data):
    empty_counter = 0
    best_counter = 0
    for point in data+['0']:
        if point == '.':
            empty_counter += 1
        if point == '0':
            if best_counter < empty_counter:
                #  print(empty_counter)
                best_counter = empty_counter
            empty_counter = 0

    best_counter -= 1
    return (int(best_counter/2), math.ceil(best_counter/2))

def save_result(filename, results):
    f = open(filename, 'w')
    for i, r in enumerate(results):
        f.write('Case #{}: {} {}'.format(i+1, r[1], r[0]))
        if i < len(results)-1:
            f.write('\n')
    f.close()

if __name__ == '__main__':
    data = parse('test7.txt')

    results = list()
    #  data = [[6, 5]]
    for i, d in enumerate(data):
        print(i)
        #  print(d)
        full_data = split(d[0]*['.'], d[1]-1)
        #  print(full_data)
        #  results.append([maxdata, mindata])
        min_max = get_best_min_max(full_data)
        results.append(min_max)
        #  print(min_max)
        reset_min_max()

    save_result('results.out', results)
