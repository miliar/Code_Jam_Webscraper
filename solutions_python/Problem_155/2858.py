__author__ = 'matee'


def sum_the_line(line):
    tmp = []
    sum = 0
    for numbers in line:
        sum += int(numbers)
        tmp.append(sum)
    #print tmp
    return tmp


def check_the_ovation(line):
    diff = [0]
    for i, j in enumerate(line):
        #print "{0}  {1}".format(i, j)
        if i > 0:
            diff.append(i - line[i-1])
    #print diff
    return diff

def read_data():
    f = open('dataset.txt')
    number_of_testcases = int(f.readline())
    data_array = []
    for line in f:
        data_array.append(line.split())
    if len(data_array) != number_of_testcases:
        print "Something is wrong with this file."
    return data_array

def write_data(filename, data_to_write):
    f = open(filename, 'w')
    for line in data_to_write:
        f.write(line + '\n')


def standing_ovation():
    data_array = read_data()
    result = []
    for i, line in enumerate(data_array):
        #print "{0} -- {1} ".format(line[0], line[1])
        summed_line = sum_the_line(line[1])
        counted_diff = check_the_ovation(summed_line)
        output_txt = 'Case #' + str(i+1) + ': ' + str(max(counted_diff))
        print output_txt
        result.append(output_txt)
        write_data("output.txt", result)



if __name__ == '__main__':
    standing_ovation()
