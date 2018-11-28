import sys

def magic(answer_1, matrix_1, answer_2, matrix_2, test_case):
    with open('output.txt', 'a') as output_file:
        set_1 = set(matrix_1[int(answer_1)].rstrip('\n').split())
        set_2 = set(matrix_2[int(answer_2)].rstrip('\n').split())
        intersection = set_1.intersection(set_2)
        if len(intersection) == 1:
            intersection = intersection.pop()
            print "Case #" + test_case + ": " + str(intersection)
            output_file.write('Case #'+test_case+': '+str(intersection)+'\n')
        elif len(intersection) > 1:
            print "Case #" + test_case + ": " + "Bad magician!"
            output_file.write('Case #'+test_case+": "+"Bad magician!"+'\n')
        elif len(intersection) == 0:
            print "Case #" + test_case + ": " + "Volunteer cheated!"
            output_file.write('Case #'+test_case+": "+"Volunteer cheated!"+'\n')

if __name__ == '__main__':
    with open(sys.argv[1]) as input_file:
        test_cases = input_file.readline()
        for test_case in range(1, int(test_cases)+1):
            answer_1 = input_file.readline()
            matrix_1 = {}
            for line in range(1, 5):
                matrix_1[line] = input_file.readline()
            answer_2 = input_file.readline()
            matrix_2 = {}
            for line in range(1, 5):
                matrix_2[line] = input_file.readline()
            magic(answer_1, matrix_1, answer_2, matrix_2, str(test_case))
