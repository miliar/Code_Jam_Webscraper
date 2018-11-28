import sys
import re

def parse_file(filename):
    with open(filename, "r") as f:
        with open("magic_trick.out", "w") as fw:
            num_test_cases_str = f.readline()
            re.sub("^.*([0-9]*).*\n$", "\\1", num_test_cases_str)
            try:
                num_test_cases = int(num_test_cases_str)
            except ValueError as e:
                print("num_test_cases_str is invalid, it is: " + str(num_test_cases_str))
                return

            print("Read number of test cases: " + str(num_test_cases))

            for test_num in range(1, num_test_cases+1):
                section1, section2 = [], []
                for i in range(5):
                    input_line = f.readline()
                    re.sub("^.*([0-9 ]*).*\n$", "\\1", input_line)
                    section1.append(input_line.strip())
                for i in range(5):
                    input_line = f.readline()
                    re.sub("^.*([0-9 ]*).*\n$", "\\1", input_line)
                    section2.append(input_line.strip())
                poss1, poss2 = interpret_section(section1), interpret_section(section2)
                intersection = poss1.intersection(poss2)

                if len(intersection) == 0:
                    result = "Volunteer cheated!"
                elif len(intersection) > 1:
                    result = "Bad magician!"
                else:
                    result = str(intersection.pop())
                fw.write("Case #" + str(test_num) + ": " + result + "\n")
                print("Wrote result of test case " + str(test_num))

def interpret_section(section):
    volunteer_answer = int(section[0])
    row_str = section[volunteer_answer]
    return set(row_str.split())



if __name__=="__main__":
    filename = sys.argv[1]
    print("Parsing file: " + str(filename))
    parse_file(filename)