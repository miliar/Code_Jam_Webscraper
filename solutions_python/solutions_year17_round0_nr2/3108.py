# Only the tidiest of numbers are allowed!
import fileinput

def find_nearest_tidy(number):
# Number must be a list of characters
    sequence_start = None
    previous = None
    
    untidy = False
    for index, digit in enumerate(number):
        if digit != previous:
            if previous is not None:
                if int(digit) < int(previous):
                    # Number is not tidy
                    untidy = True
                    break
            
            sequence_start = index
        
        previous = digit
    
    if untidy:
        # Decrement sequence start by one
        number[sequence_start] = str(int(number[sequence_start]) - 1)
        
        # Replace tail with all 9s
        for index in range(sequence_start+1, len(number)):
            number[index] = '9'
    
    return int(''.join(number))

def main():
    have_read_first_line = False
    case = 1
    
    for line in fileinput.input():
        if not have_read_first_line:
            have_read_first_line = True
            continue
        
        number = list(line.strip())
        
        # Print case, stripping leading zeros lazily
        print('Case #' + str(case) + ': ' + str(find_nearest_tidy(number)))
        case += 1

if __name__ == '__main__':
    main()