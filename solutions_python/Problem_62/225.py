def int_input():
    return int(raw_input())

def list_int_input():
    return map(int, raw_input().split())

def get_input():
    size = int_input()
    lines = []
    for i in range(size):
        lines.append(list_int_input())
    return size, lines

def count_higher_right(value, rights):
    counter = 0
    for n in reversed(rights):
        if n > value:
            counter += 1
        else:
            break
    return counter

def get_answer(size, lines):
    lines.sort()
    rights = []
    max_right = 0
    answer = 0
    for line in lines:
        if line[1] < max_right:
            answer += count_higher_right(line[1], rights)
        max_right = max(max_right, line[1])
        rights.append(line[1])
        rights.sort()
    return answer

def print_answer(case, answer):
    print "Case #%d: %d" % (case, answer)

def main():
    for case in range(int_input()):
        size, lines = get_input()
        answer = get_answer(size, lines)
        print_answer(case+1, answer)

main()
