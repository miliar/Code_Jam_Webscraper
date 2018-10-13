import math

def is_fair(number):
    word = str(number)
    last_i = len(word)-1
    for i in range(0, last_i/2+1):
        if word[i] != word[last_i-i]:
            return False
    return True


def process_case(input_line):
    int1, int2 = map(int, input_line.split())
    answer = 0
    for number in range(int1, int2+1):
        root = math.sqrt(number)
        int_root = math.trunc(root)
        if root == int_root:
            if is_fair(int_root):
                if is_fair(number):
                    answer += 1
    return answer

def process_input():
    number_of_cases = int(raw_input())
    for case_number in range(1, number_of_cases + 1):
        input_line = raw_input()
        answer = process_case(input_line)
        print 'Case #%d: %d' % (case_number, answer)

if __name__ == '__main__':
    process_input()

