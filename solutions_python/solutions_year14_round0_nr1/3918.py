import sys
import os

def match_rows(row1, row2):
    result = [];
    for e1 in row1:
        if e1 in row2:
            result.append(e1)
        if (len(result) > 1):
            break
    return result

def output_testresult(f_out, test, match):
    if len(match) == 0:
        result = 'Volunteer cheated!'
    elif len(match) == 1:
        result = str(match[0])
    else:
        result = 'Bad magician!'
    output = 'Case #{test}: {result}\n'.format(test=test, result=result)
    f_out.write(output)
    
def get_row(f_in):
    row = int(f_in.readline()) - 1;
    row_content = []
    for r in range(4):
        line = f_in.readline()
        if (r == row):
            row_content = [int(token) for token in line.split()]
    return row_content

def get_output_filename(input_file):
    path = os.path.splitext(input_file)
    return path[0] + '.out'

def main(input_file):
    with open(input_file, "U") as f_in:
        with open(get_output_filename(input_file), "w") as f_out:
            T = int(f_in.readline())
            for test in range(1, T+1):
                first_row = get_row(f_in)
                second_row = get_row(f_in)
                match = match_rows(first_row, second_row)
                output_testresult(f_out, test, match)
            
    
if __name__ == "__main__":
    main(sys.argv[1])
