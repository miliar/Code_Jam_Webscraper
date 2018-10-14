import csv

def create_dictionary_file(input_filename, output_filename):
    translation = {}
    f = open(input_filename, 'r')
    max_lines = int(f.readline())
    print max_lines
    line_number = 0
    while line_number < max_lines:
        line = f.readline()
        line.strip()
        print line
        for i in range(0, len(line)):
            key = line[i]
            value  = getchar(output_filename, line_number, i)
            print "[%s] => %s" % (key, value)
            translation[key] = value
        line_number +=  1
    print translation.keys()
    print len(translation.keys())

    dictWriter = csv.writer(open('googlerese.csv', 'w'))
    for k,v in translation.iteritems():
        dictWriter.writerow([k,v])

def run_test(input_filename):
    #build dictinoary
    googlereseReader = csv.reader(open('googlerese.csv', 'r'))
    dictionary = {}

    for row in googlereseReader:
        key = row[0]
        value = row[1]
        dictionary[key] = value

    print dictionary

    fin = open(input_filename, 'r')
    fout = open("output_%s.txt" % input_filename, 'w')
    
    max_lines = int(fin.readline())
    print max_lines
    line_number = 0
    while line_number < max_lines:
        line = fin.readline()
        line.strip()
        print line
        output_chars = []
        for i in range(0, len(line)):
            key = line[i]
            if key in dictionary:
                output_chars.append(dictionary[key])
            else: 
                output_chars.append(key)
        output_line = "".join(output_chars)
        print output_line
        fout.write("Case #%d: %s" % (line_number + 1, output_line))
        line_number +=  1


def getchar(output_filename, line_number, char_index):
    f = open(output_filename, 'r')
    c_line_number = 0
    line = ""
    while c_line_number <= line_number:
        line = f.readline()
        c_line_number += 1

    # print line
    return line[char_index]


if __name__ == '__main__':
    # create_dictionary_file("input_test.txt","output_test.txt")
    # run_test("input_test.txt")
    run_test("A-small-attempt2.in")



