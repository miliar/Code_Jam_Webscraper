import random
import sys

def generate_test_data():
    cases = random.randint(5, 100)
    print "{} cases".format(cases)
    data = "{}\n".format(cases)

    for x in range(cases):
        data += "{}\n".format(random.randint(1, 1000))

    return data.strip()

def test(test_data):
    data = [int(x) for x in list(test_data)]
    index = len(test_data) -1
    while index > 0:
        if data[index] < data[index-1]:
            for i in range(len(data) - index):
                data[index + i] = 9
            data[index-1] = data[index-1] - 1
        index -= 1

    raw_result = "".join([str(x) for x in data])

    return int(raw_result)

if __name__ == '__main__':

    if sys.argv[1] == 'gen_data':
        with open('test_data', 'w+') as outfile:
            outfile.write(generate_test_data())            
        sys.exit(1)

    infile = open(sys.argv[1])
    data = ""
    with open(sys.argv[1] + '_out', 'w+') as outfile:
        for i in range(int(infile.readline())):
            test_data = infile.readline().strip()
            solution = test(test_data)
            data += 'Case #{}: {}\n'.format(i+1, solution)
        outfile.write(data.strip())