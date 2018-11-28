import sys

def find_tidy_number(number):
    tidy_number = ""
    i = 0
    if len(number) == 1:
        return number

    max_pos = 0
    while len(tidy_number) < len(number) and i < len(number):
        if i == len(number)-1:
            tidy_number += number[i]
        elif number[i] <= number[i + 1]:
            tidy_number += number[i]
            if number[max_pos] < number[i]:
                max_pos = i
        else:
            new_num = str(int(number[i])-1)
            if number[max_pos] > new_num:
                new_num = str(int(number[max_pos]) - 1)
                tidy_number = tidy_number[0:max_pos]
                tidy_number += new_num
                for j in range(max_pos + 1, len(number)):
                    tidy_number += "9"
            else:    
                tidy_number += new_num
                for j in range(i + 1, len(number)):
                    tidy_number += "9"
        i += 1
    
    return int(tidy_number)

if __name__ == '__main__':
    num_cases = int(sys.stdin.readline().strip())
    case = 0
    while True:
        case += 1
        line = sys.stdin.readline().strip()
        if line == '':
            break
        print("Case #" + str(case) + ": " + str(find_tidy_number(line)))