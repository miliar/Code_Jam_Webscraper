import sys


def process_file(input_file, output_file):
    file_in = open(input_file, 'rU')
    file_out = open(output_file, 'w')

    
    i = 0
    num_cases = None
    case_num = 0
    answer_1 = None
    answer_2 = None
    card_set_1 = None
    card_set_2 = None

    for row in file_in:
        
        if not num_cases:
            num_cases = int(row)

        elif i % 10 == 1:
            case_num += 1
            answer_1 = int(row)

        elif i % 10 == 6:
            answer_2 = int(row)

        elif answer_1 and i % 10 == answer_1 + 1:
            card_set_1 = [int(n) for n in (row.strip()).split(' ')]

        elif answer_2 and i % 10 == ((answer_2 + 6) % 10):
            card_set_2 = [int(n) for n in (row.strip()).split(' ')]

        if i > 0 and i % 10 == 0:
            matched_numbers = [n for n in card_set_1 if n in card_set_2]
            if len(matched_numbers) == 0:
                result = 'Case #' + str(case_num) + ': Volunteer cheated!'
            elif len(matched_numbers) == 1:
                result = 'Case #' + str(case_num) + ': ' + str(matched_numbers[0])
            else:
                result = 'Case #' + str(case_num) + ': Bad magician!'
            
            file_out.write(result+'\n')

        i += 1
        
    file_out.close()
            

def main():
    if len(sys.argv) == 3:
        print 'Program starts'
        process_file(sys.argv[1], sys.argv[2])
        sys.exit(1)
        
    else:
        print 'Give two arguments (INPUT_FILE OUTPUT_FILE)'
        sys.exit(1)


if __name__ == '__main__':
    main()
